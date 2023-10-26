import unittest
from src.dinasore.resources.function_blocks.MES.MOVING_AVERAGE_V2 import MOVING_AVERAGE_V2

class TestMOVING_AVERAGE_V2(unittest.TestCase):
    def setUp(self):
        self.moving_average_v2 = MOVING_AVERAGE_V2()
    
    def tearDown(self):
        del self.moving_average_v2

    def test_schedule_init(self):
        event_name = 'INIT'
        event_value = None
        window = 5
        sensor_id = 'sensor_id'
        value = 1
        
        expected = [event_value, None, 0, 0]

        actual = self.moving_average_v2.schedule(event_name, event_value, window, sensor_id, value)
        
        self.assertEqual(actual, expected)
        
        # assert values_dict is initialized
        self.assertEqual(self.moving_average_v2.values_dict, {sensor_id: []})
        
    def test_schedule_run(self):
        event_name = 'RUN'
        event_value = None
        window = 5
        sensor_id = 'sensor_id'
        value = 1
        
        expected = [None, event_value, 0, 0]

        actual = self.moving_average_v2.schedule(event_name, event_value, window, sensor_id, value)
        
        self.assertEqual(actual, expected)
        
        # assert values_dict is initialized
        self.assertEqual(self.moving_average_v2.values_dict, {sensor_id: [value]})
        
    def test_schedule_run_2(self):
        event_name = 'RUN'
        event_value = None
        window = 5
        sensor_id = 'sensor_id'
        value = 5
        
        expected = [None, event_value, sensor_id, 3]

        self.moving_average_v2.values_dict = {sensor_id: [1, 2, 3, 4]}
        actual = self.moving_average_v2.schedule(event_name, event_value, window, sensor_id, value)
        
        self.assertEqual(actual, expected)
        
        # assert values_dict is initialized
        self.assertEqual(self.moving_average_v2.values_dict, {sensor_id: [2, 3, 4, 5]})
        
