import numpy as np
import time
import psycopg2


def create_distribution(offset=0, max_samples=300):
    # generate values based in the normal distribution
    mu, sigma = 0.5, 0.1
    s = np.random.normal(mu, sigma, 3000)
    # organizes the values in a normal curve
    hist, _ = np.histogram(s, bins=np.arange(0.2, 0.8, 0.002))
    values2sort = offset + (hist / 4)
    # split the array to start in a random place
    split_value = np.random.randint(0, max_samples)
    final_values = np.concatenate(
        [values2sort[split_value:], values2sort[0:split_value]])
    return final_values


def create_distribution_within_range(min_value=10, max_value=100, offset=0, max_samples=300):
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


class SENSOR_SIMULATOR_V2:

    MAX_RETRIES = 10
    RETRY_DELAY_SECONDS = 5
    MAX_SAMPLES = 300

    def __init__(self):
        self.distribution = None
        self.distribution_index = 0
        self.data = None
        self.data_length = 0
        self.curr_sensor_index = 0
        self.sensor_thresholds = []  # [(sensor_id, min_value, max_value)]}
        self.sensor_data = []  # {[(sensor_id,[values])]

    def __db_connection(self):
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
                    print(
                        f"An error occurred: {e}. Retrying in {self.RETRY_DELAY_SECONDS} seconds...")
                    time.sleep(self.RETRY_DELAY_SECONDS)
                else:
                    print(f"Max retries reached. An error occurred: {e}")
                    raise e

    def __fetch_sensors_data(self):
        connection = None
        cursor = None
        try:
            print("Connecting to the database...")
            connection = self.__db_connection()

            if not connection:
                raise Exception("No connection to database")

            cursor = connection.cursor()
            print("Fetching sensors data...")
            cursor.execute("""
                select s.id, sm.min_value, sm.max_value from sensor s
                inner join sensor_model sm on s.sensor_model_id = sm.id
            """)
            return cursor.fetchall()
        except Exception as e:
            print(f"An error occurred: {e}")
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
            self.data = self.__fetch_sensors_data()
            print('Sensors data fetched')

            if not self.data:
                print('No sensors data')
                raise Exception("No sensors data")

            self.data_length = len(self.data)

            for sensor_id, min_value, max_value in self.data:
                self.sensor_thresholds.append(
                    (sensor_id, min_value, max_value))

            return [event_value, None, 0, 0]

        elif event_name == 'READ':

            # print('Reading sensor data...')
            try:
                if self.curr_sensor_index >= self.data_length:
                    self.curr_sensor_index = 0
                    self.distribution_index += 1

                    if self.distribution_index >= self.MAX_SAMPLES:
                        self.distribution_index = 0
                if self.curr_sensor_index >= len(self.sensor_data):
                    sensor_id, min_value, max_value = self.sensor_thresholds[self.curr_sensor_index]
                    self.sensor_data.append((sensor_id, create_distribution_within_range(
                        min_value, max_value, offset, self.MAX_SAMPLES)))
                    # print('Sensor data read')

                sensor_id, values = self.sensor_data[self.curr_sensor_index]
                value = values[self.distribution_index]

                self.curr_sensor_index += 1

                # wait some time
                time.sleep(5/(self.data_length + 1))

                # print(f"Current indexes: Sensor - {self.curr_sensor_index} ;;;;;; Distribution - {self.distribution_index}, Sensor '{sensor_id}' value: {value}")

                return [None, event_value, sensor_id, value]
            except Exception as e:
                print(f"An error occurred: {e}")
                return [None, None, None, None]
