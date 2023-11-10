import numpy as np
import time
import psycopg2

# TODO: save fault_state and last value of 'IncrementalFaultValue' for each sensor

DEFAULT_STEP_AIR_FLOW = 0.8
DEFAULT_STEP_PRESSURE = 0.8
DEFAULT_STEP_TEMP = 0.8

DEFAULT_NOISE_LEVEL_AIR_FLOW = 0.05
DEFAULT_NOISE_LEVEL_PRESSURE = 0.01
DEFAULT_NOISE_LEVEL_TEMP= 1.2

DEFAULT_AIR_FLOW_VALUES = [
    (0, 0.3),
    (4, 0.3),
    (6, 3.3),
    (7, 2.2),
    (17, 1.7),
    (22, 1.6),
    (27, 1.7),
    (35, 1.6),
    (50, 1.6),
    (55, 1),
    (60, 0.7),
    (70, 0.3),
    (100, 0.3)
]

DEFAULT_TEMP_VALUES = [
    (0, 26),
    (4, 27),
    (8, 26),
    (9, 42),
    (10, 53),
    (11, 60),
    (12, 65),
    (13, 70),
    (14.2, 75),
    (15.5, 80),
    (17, 83),
    (19, 85),
    (22, 88),
    (25, 89),
    (30, 90),
    (46, 90),
    (48, 75),
    (49, 70),
    (51, 63),
    (52, 63),
    (53, 70),
    (55.5, 80),
    (57, 83),
    (59, 85),
    (62, 88),
    (65, 89),
    (80, 90),
    (86, 90),
    (88, 75),
    (89, 70),
    (91, 63),
    (93, 58),
    (97, 48),
    (100, 44),
    (105, 39),
    (110, 35), 
    (120, 30), 
    (140, 26),
    (150, 26)
]

DEFAULT_PRESSURE_VALUES = [
    (0, 0.1),
    (4, 0.1),
    (6, 1.6),
    (12, 1.6),
    (13, 0.82),
    (22, 0.8),
    (27, 0.82),
    (35, 0.8),
    (50, 0.8),
    (51, 0.5),
    (60, 0.5),
    (69, 0.5),
    (70, 0.1),
    (100, 0.1)
]

DEFAULT_VALUES = {
    'flow': (DEFAULT_STEP_AIR_FLOW, DEFAULT_NOISE_LEVEL_AIR_FLOW, DEFAULT_AIR_FLOW_VALUES),
    'temperature': (DEFAULT_STEP_TEMP, DEFAULT_NOISE_LEVEL_TEMP, DEFAULT_TEMP_VALUES),
    'pressure': (DEFAULT_STEP_PRESSURE, DEFAULT_NOISE_LEVEL_PRESSURE, DEFAULT_PRESSURE_VALUES)
}
    
class IncrementalFaultValue:
    def __init__(self, target, step = 0.05, time_step = 0.1, value = 0) -> None:
        """
        Step: the multiplier of target to increment the value.
        """
        self.value = 0
        self.target = target
        self.step = step * time_step * target

    def _update_value(self):
        self.value = self.value + self.step if self.value + self.step <= self.target else self.target

    def reset(self):
        self.value = 0

    def get_current_value(self):
        """
        The value is updated every time this method is called.
        """
        self._update_value()
        return self.value
    
def repeat_values_n_times(values, N):

    if N <= 1:
        return values

    timestamp_increment = values[-1][0]
    
    # Initialize the result array with the original air_flow_values
    result = values[:]
    
    for i in range(1, N):
        # Create the new repeated sequence, adjusting timestamps with the increment
        new_sequence = [(t + i * timestamp_increment, v) for t, v in values[1:]]
        # Append the new sequence to the result
        result.extend(new_sequence)
    
    return result

def simulate_faults(values = [], fault_rate = 0.1, fault_duration= 0.25, fault_type = 'distinct', step = 0.05, type = 'temperature', fault_value_growth= 1.0, fault_state= 'normal'):
    """
    Simulate faults for the given values.
    After the system enters a fault state, the kind of failure is chosen randomly and stays in that state for a random time.
    fault_type: 'continuous', 'distinct'. Continuous faults are not reset until the end of the simulation.
    """

    # Initialize the result array with the original air_flow_values
    result = []

    # Initialize the fault timer
    fault_timer = 0

    min_temp = min([v for _, v in values])
    max_temp = max([v for _, v in values])
    value_interval = max_temp - min_temp
    time_interval = (values[-1][0] - values[0][0])
    target_fault_value = value_interval/8
    incremental_fault_value = IncrementalFaultValue(target_fault_value, step = 0.05, time_step = step)

    # Iterate over the original values
    for (t, v) in values:
        # If the system is in a fault state
        if fault_state != 'normal':
            # If the fault timer has reached 0, the system is back to normal
            if fault_type == 'distinct':
                if fault_timer <= 0:
                    fault_state = 'normal'
                    incremental_fault_value.reset()
                else:
                    # Otherwise, the fault timer is decremented
                    fault_timer -= step
        else:
            # Otherwise, the system is normal and a fault can occur
            if np.random.random() < fault_rate*step:
                # If a fault occurs, the fault state is set to a random value

                if v < min_temp + value_interval/10:
                    fault_state = 'high'
                elif v > max_temp - value_interval/10:
                    fault_state = 'low'
                else:
                    fault_state = np.random.choice(['high', 'low'])

                # The fault timer is set to a random value
                fault_timer = fault_duration*time_interval if fault_duration > 0 else  np.random.random()*time_interval + time_interval/24

        # If the system is in a fault state, the value is modified
        if fault_state == 'high':
            v += incremental_fault_value.get_current_value()*fault_value_growth
        elif fault_state == 'low':
            v -= incremental_fault_value.get_current_value()*fault_value_growth
            if type != 'temperature':
                v = 0 if v < 0 else v

        # The value is appended to the result
        result.append((t, v))

    return result, fault_state

def interpolate_with_noise(values, step=0.05, noise_level=0.1):
    interpolated_values = []
    for i in range(len(values) - 1):
        # Unpack the current and next tuple
        (t1, temp1), (t2, temp2) = values[i], values[i + 1]

        # Calculate the number of steps between the two times
        steps = range(1, int(round((t2 - t1) / step)))

        # Find the temperature difference and set a minimum difference threshold
        temps_diff = max(np.fabs(temp2 - temp1), 0.05)

        # Modify the noise level based on the temperature difference
        # The noise level is higher for smaller differences and lower for larger differences
        adjusted_noise_level = noise_level / (1 + temps_diff)

        # Generate the intermediate values with noise
        for i, s in enumerate(steps, start=1):
            # Calculate the intermediate time
            current_time = t1 + s * step

            # Linear interpolation formula
            current_temp = temp1 + ((temp2 - temp1) / (t2 - t1)) * (current_time - t1)

            denominator = np.exp(-i + 1) + 1.5

            # Introduce noise
            noise = np.random.uniform(-adjusted_noise_level/denominator, adjusted_noise_level/denominator)
            current_temp_with_noise = current_temp + noise

            # Append the interpolated value to the list
            interpolated_values.append((round(current_time, 2), current_temp_with_noise))

        # Add the last value of the current interval if it's not the last tuple
        if i < len(values) - 2:
            interpolated_values.append((t2, temp2 + np.random.uniform(-adjusted_noise_level, adjusted_noise_level)))

    # Append the last value of the entire sequence with noise
    final_time, final_temp = values[-1]
    interpolated_values.append((final_time, final_temp + np.random.uniform(-adjusted_noise_level, adjusted_noise_level)))

    return interpolated_values

def create_distribution_(type = ''):
    fault_state = 'normal'
    match type:
        case 'Temperature':
            type = 'temperature'
            step, noise_level, values = DEFAULT_VALUES[type]
            interpolated_values = interpolate_with_noise(values, step, noise_level)
            interpolated_values, fault_state = simulate_faults(interpolated_values, fault_rate = np.random([0,0.5]), fault_type='continuous', fault_value_growth= np.random([0.5,4]), fault_state= fault_state)
            
            pass
        case _: return

def create_distribution(offset=0, max_samples = 300):
    # generate values based in the normal distribution
    mu, sigma = 0.5, 0.1
    s = np.random.normal(mu, sigma, 3000)
    # organizes the values in a normal curve
    hist, _ = np.histogram(s, bins=np.arange(0.2, 0.8, 0.002))
    values2sort = offset + (hist / 4)
    # split the array to start in a random place
    split_value = np.random.randint(0, max_samples)
    final_values = np.concatenate([values2sort[split_value:], values2sort[0:split_value]])
    return final_values

def create_distribution_within_range(min_value=10, max_value=100, offset=0, max_samples = 300):
    final_values = create_distribution(offset, max_samples)
    
    # Current range of the data
    a = np.min(final_values)
    b = np.max(final_values)
    
    # Desired range [c, d]
    c, d = min_value, max_value
    
    # Applying the linear transformation
    transformed_values = c + (final_values - a) * (d - c) / (b - a)

    # Final values with only 2 decimal places
    transformed_values = np.round(transformed_values, 2)
    
    return transformed_values


class SENSOR_SIMULATOR_V3:

    MAX_RETRIES = 10
    RETRY_DELAY_SECONDS = 5
    MAX_SAMPLES = 300

    def __init__(self):
        self.distribution = None
        self.distribution_index = 0
        self.data = None
        self.data_length = 0
        self.curr_sensor_index = 0
        self.sensor_thresholds = [] # [(sensor_id, min_value, max_value)]}
        self.sensor_data = [] # {[(sensor_id,[values])]

    def _db_connection(self):
        for attempt in range(self.MAX_RETRIES):
            print(f"Attempt {attempt}: Connecting to the database")
            try:
                connection = psycopg2.connect(
                    dbname='postgres',
                    user='postgres',
                    password='postgres',
                    host='localhost',
                    port='5432'
                )
                print("Successfully connected to the database")
                return connection
            except Exception as e:
                print(f"An error occurred: {e}")
                if attempt < self.MAX_RETRIES:
                    print(f"An error occurred: {e}. Retrying in {self.RETRY_DELAY_SECONDS} seconds...")
                    time.sleep(self.RETRY_DELAY_SECONDS)
                else:
                    print(f"Max retries reached. An error occurred: {e}")
                    raise e
                
    def _fetch_sensors_data(self):
        connection = None
        cursor = None
        try:
            print("Connecting to the database...")
            connection = self._db_connection()

            if not connection:
                raise Exception("No connection to database")
            
            cursor = connection.cursor()
            print("Fetching sensors data...")

            cursor.execute("""
                select s.id, sm.min_value, sm.max_value from sensor s
                inner join sensor_model sm on s.sensor_model_id = sm.id
            """)
            
            self.data = cursor.fetchall()
        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            if cursor:
                cursor.close()
            if connection:
                connection.close()

    def schedule(self, event_name, event_value, offset):
        if event_name == 'INIT':
            self.distribution_index = 0
            print('Fetching sensors data...')
            self._fetch_sensors_data()
            print('Sensors data fetched')
            
            if not self.data:
                print('No sensors data')
                raise Exception("No sensors data")
            
            self.data_length = len(self.data)

            for sensor_id, min_value, max_value in self.data:
                self.sensor_thresholds.append((sensor_id, min_value, max_value))
            
            return [event_value, None, 0, 0]

        elif event_name == 'READ':

            try:
                if self.curr_sensor_index >= self.data_length:
                    self.curr_sensor_index = 0
                    self.distribution_index += 1

                    if self.distribution_index >= self.MAX_SAMPLES:
                        self.distribution_index = 0
                if self.curr_sensor_index >= len(self.sensor_data):
                    sensor_id, min_value, max_value = self.sensor_thresholds[self.curr_sensor_index]
                    self.sensor_data.append((sensor_id, create_distribution_within_range(min_value, max_value, offset, self.MAX_SAMPLES)))

                sensor_id, values = self.sensor_data[self.curr_sensor_index]
                value = values[self.distribution_index]

                self.curr_sensor_index += 1

                # wait some time
                time.sleep(5/(self.data_length + 1))

                return [None, event_value, sensor_id, value]
            
            except Exception as e:
                print(f"An error occurred: {e}")
                return [None, None, None, None]