import unittest
from unittest.mock import patch, MagicMock
from src.dinasore.resources.function_blocks.MES.PROMETHEUS_WRITER import PROMETHEUS_WRITER

class Test_PROMETHEUS_WRITER(unittest.TestCase):
    def setUp(self):
        self.writer = PROMETHEUS_WRITER()
        
    
    def tearDown(self):
        del self.writer
    
    @patch('src.dinasore.resources.function_blocks.MES.PROMETHEUS_WRITER.CollectorRegistry')
    @patch('src.dinasore.resources.function_blocks.MES.PROMETHEUS_WRITER.Gauge')
    def test_schedule_init(self, mock_gauge, mock_registry):
        event_name = 'INIT'
        event_value = 1
        host = 'localhost'
        port = 9091
        value_name_1 = 'value_1'
        value_1 = 1
        value_name_2 = 'value_2'
        value_name_2_descr = 'value_2_description'
        value_2 = 2.0
        value_name_3 = 'value_3'
        value_name_3_descr = 'value_3_description'
        value_3 = 3.0
        job_name = 'job_name'
        
        expected = [event_value, None]

        actual = self.writer.schedule(event_name, event_value,
                 host, port,
                 value_name_1, value_name_2, value_name_2_descr, value_name_3, value_name_3_descr, job_name,
                 value_1, value_2, value_3)
        
        self.assertEqual(actual, expected)
        
        #assert number of calls to mock_registry
        self.assertEqual(mock_registry.call_count, 1)
        self.assertEqual(mock_registry.call_args, ())
       
        #assert number of calls to mock_gauge
        self.assertEqual(mock_gauge.call_count, 2)
        self.assertEqual(mock_gauge.call_args_list[0][0], (value_name_2, value_name_2_descr, [value_name_1]))
        self.assertEqual(mock_gauge.call_args_list[1][0], (value_name_3, value_name_3_descr, [value_name_1]))

        self.assertEqual(self.writer.JOB_NAME, job_name)
        self.assertEqual(self.writer.PUSHGATEWAY_ADDRESS, f"{host}:{port}")

    @patch('src.dinasore.resources.function_blocks.MES.PROMETHEUS_WRITER.CollectorRegistry')
    @patch('src.dinasore.resources.function_blocks.MES.PROMETHEUS_WRITER.Gauge')
    def test_schedule_init_failure(self, mock_gauge, mock_registry):
        # mock exception
        mock_registry.side_effect = Exception('Registry exception')

        event_name = 'INIT'
        event_value = None
        host = 'localhost'
        port = 9091
        value_name_1 = 'value_1'
        value_1 = 1
        value_name_2 = 'value_2'
        value_name_2_descr = 'value_2_description'
        value_2 = 2.0
        value_name_3 = 'value_3'
        value_name_3_descr = 'value_3_description'
        value_3 = 3.0
        job_name = 'job_name'
        
        expected = [event_value, None]

        actual = self.writer.schedule(event_name, event_value,
                 host, port,
                 value_name_1, value_name_2, value_name_2_descr, value_name_3, value_name_3_descr, job_name,
                 value_1, value_2, value_3)
        
        self.assertEqual(actual, expected)
        
        # assert exception is raised
        self.assertEqual(mock_registry.call_count, 1)
        self.assertEqual(mock_registry.call_args, ())
        self.assertEqual(mock_gauge.call_count, 0)

        # assert JOB_NAME and PUSHGATEWAY_ADDRESS do not exist
        self.assertFalse(hasattr(self.writer, 'JOB_NAME'))
        self.assertFalse(hasattr(self.writer, 'PUSHGATEWAY_ADDRESS'))

    @patch('src.dinasore.resources.function_blocks.MES.PROMETHEUS_WRITER.push_to_gateway')
    def test_schedule_run(self, mock_push_to_gateway):
        # prepare mocks
        mock_push_to_gateway.return_value = None
        self.writer.registry = MagicMock()
        self.writer.SENSOR_VALUE = MagicMock()
        self.writer.MOVING_AVERAGE = MagicMock()
        self.writer.SENSOR_VALUE.labels.set.return_value = None
        self.writer.MOVING_AVERAGE.labels.set.return_value = None
        self.writer.JOB_NAME = 'job_name'
        self.writer.PUSHGATEWAY_ADDRESS = 'localhost:9091'

        event_name = 'RUN'
        event_value = 1
        host = 'localhost'
        port = 9091
        value_name_1 = 'value_1'
        value_1 = 1
        value_name_2 = 'value_2'
        value_name_2_descr = 'value_2_description'
        value_2 = 2.0
        value_name_3 = 'value_3'
        value_name_3_descr = 'value_3_description'
        value_3 = 3.0
        job_name = 'job_name'
        
        expected = [None, event_value]

        actual = self.writer.schedule(event_name, event_value,
                 host, port,
                 value_name_1, value_name_2, value_name_2_descr, value_name_3, value_name_3_descr, job_name,
                 value_1, value_2, value_3)
        
        self.assertEqual(actual, expected)
        
        # assert number of calls to mock_push_to_gateway
        self.assertEqual(mock_push_to_gateway.call_count, 1)
        self.assertEqual(mock_push_to_gateway.call_args, ((f"{host}:{port}",), {'job': job_name, 'registry': self.writer.registry}))

    @patch('src.dinasore.resources.function_blocks.MES.PROMETHEUS_WRITER.push_to_gateway')
    def test_schedule_run(self, mock_push_to_gateway):
        # prepare mocks
        mock_push_to_gateway.return_value = None
        mock_push_to_gateway.side_effect = Exception('Push to gateway exception')
        self.writer.registry = MagicMock()
        self.writer.SENSOR_VALUE = MagicMock()
        self.writer.MOVING_AVERAGE = MagicMock()
        self.writer.SENSOR_VALUE.labels.set.return_value = None
        self.writer.MOVING_AVERAGE.labels.set.return_value = None
        self.writer.JOB_NAME = 'job_name'
        self.writer.PUSHGATEWAY_ADDRESS = 'localhost:9091'

        event_name = 'RUN'
        event_value = 1
        host = 'localhost'
        port = 9091
        value_name_1 = 'value_1'
        value_1 = 1
        value_name_2 = 'value_2'
        value_name_2_descr = 'value_2_description'
        value_2 = 2.0
        value_name_3 = 'value_3'
        value_name_3_descr = 'value_3_description'
        value_3 = 3.0
        job_name = 'job_name'
        
        expected = [None, event_value]

        actual = self.writer.schedule(event_name, event_value,
                 host, port,
                 value_name_1, value_name_2, value_name_2_descr, value_name_3, value_name_3_descr, job_name,
                 value_1, value_2, value_3)
        
        self.assertEqual(actual, expected)
        
        # assert number of calls to mock_push_to_gateway
        self.assertEqual(mock_push_to_gateway.call_count, 1)
        self.assertEqual(mock_push_to_gateway.call_args, ((f"{host}:{port}",), {'job': job_name, 'registry': self.writer.registry}))
        
    