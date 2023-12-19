
import random

class IncrementalFaultValue:
    def __init__(self, target, step = 0.5, time = 10, time_step = 0.1) -> None:
        """
        Step: the multiplier of target to increment the value.
        """
        self.value = 0
        self.target = target
        self.step = step * time_step * target
        self.time = time
        self.time_step = time_step
        self.curr_time = 0
    
    def _update_time(self):
        self.curr_time += self.time_step

    def _update_value(self):
        self._update_time()
        self.value = self.value + self.step if self.value + self.step <= self.target else self.target

    def reset(self):
        self.value = 0
        self.curr_time = 0

    def get_current_value(self):
        """
        The value is updated every time this method is called.
        """
        self._update_value()
        return self.value

def simulate_faults(values = [], fault_rate = 0.1, fault_duration= 0.25, fault_type = 'distinct', step = 0.05, type = 'temperature', fault_value_growth= 1.0):
    """
    Simulate faults for the given values.
    After the system enters a fault state, the kind of failure is chosen randomly and stays in that state for a random time.
    fault_type: 'continuous', 'distinct'. Continuous faults are not reset until the end of the simulation.
    """

    # Initialize the result array with the original air_flow_values
    result = []

    # Initialize the fault state
    fault_state = 'normal'

    # Initialize the fault timer
    fault_timer = 0

    min_temp = min([v for _, v in values])
    max_temp = max([v for _, v in values])
    value_interval = max_temp - min_temp
    time_interval = (values[-1][0] - values[0][0])
    target_fault_value = value_interval/8
    incremental_fault_value = IncrementalFaultValue(target_fault_value, step = 0.05, time = int(time_interval*fault_duration), time_step = step)

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
            if random.random() < fault_rate*step:
                # If a fault occurs, the fault state is set to a random value

                if v < min_temp + value_interval/10:
                    fault_state = 'high'
                elif v > max_temp - value_interval/10:
                    fault_state = 'low'
                else:
                    fault_state = random.choice(['high', 'low'])

                # The fault timer is set to a random value
                fault_timer = random.random()*time_interval + time_interval/24

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


def test_simulate_faults():
    # Test normal behavior with no faults
    values = [(0, 20), (1, 25), (2, 30), (3, 35), (4, 40)]
    result, fault_state = simulate_faults(values, fault_rate=0.0, step=1,)
    assert result == values
    assert fault_state == 'normal'

    # Test distinct fault
    values = [(0, 20), (1, 25), (2, 30), (3, 35), (4, 40)]
    result, fault_state = simulate_faults(values, fault_rate=1.0, fault_duration=0.1, step=1, fault_type='distinct')
    assert result != values

    # Test continuous fault
    values = [(0, 20), (1, 25), (2, 30), (3, 35), (4, 40)]
    result, fault_state = simulate_faults(values, fault_rate=1.0, fault_duration=1.0, step=1, fault_type='continuous')
    assert result != values
    assert fault_state != 'normal'


if __name__ == '__main__':
    n = 100
    for _ in range(n):
        test_simulate_faults()
    print(f'{n} tests passed successfuly!')