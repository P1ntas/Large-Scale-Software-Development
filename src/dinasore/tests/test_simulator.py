import pytest

import matplotlib.pyplot as plt
import random
import math

DEFAULT_STEP_AIR_FLOW = 0.05
DEFAULT_STEP_PRESSURE = 0.04
DEFAULT_STEP_TEMP = 0.8

DEFAULT_NOISE_LEVEL_AIR_FLOW = 0.05
DEFAULT_NOISE_LEVEL_PRESSURE = 0.01
DEFAULT_NOISE_LEVEL_TEMP= 1.2

DEFAULT_AIR_FLOW_VALUES = [
    (0, 0.3),
    (0.4, 0.3),
    (0.6, 3.3),
    (0.7, 2.2),
    (1.7, 1.7),
    (2.2, 1.6),
    (2.7, 1.7),
    (3.5, 1.6),
    (5, 1.6),
    (5.5, 1),
    (6, 0.7),
    (7, 0.3),
    (10, 0.3)
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
    (0.4, 0.1),
    (0.6, 1.6),
    (1.2, 1.6),
    (1.3, 0.82),
    (2.2, 0.8),
    (2.7, 0.82),
    (3.5, 0.8),
    (5, 0.8),
    (5.1, 0.5),
    (6, 0.5),
    (6.9, 0.5),
    (7, 0.1),
    (10, 0.1)
]

DEFAULT_VALUES = {
    'flow': (DEFAULT_STEP_AIR_FLOW, DEFAULT_NOISE_LEVEL_AIR_FLOW, DEFAULT_AIR_FLOW_VALUES),
    'temperature': (DEFAULT_STEP_TEMP, DEFAULT_NOISE_LEVEL_TEMP, DEFAULT_TEMP_VALUES),
    'pressure': (DEFAULT_STEP_PRESSURE, DEFAULT_NOISE_LEVEL_PRESSURE, DEFAULT_PRESSURE_VALUES)
}

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

def simulate_faults(values = DEFAULT_TEMP_VALUES.copy(), fault_rate = 0.1, fault_duration= 0.25, fault_type = 'distinct', step = 0.05, type = 'temperature'):
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
            v += incremental_fault_value.get_current_value()
        elif fault_state == 'low':
            v -= incremental_fault_value.get_current_value()
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