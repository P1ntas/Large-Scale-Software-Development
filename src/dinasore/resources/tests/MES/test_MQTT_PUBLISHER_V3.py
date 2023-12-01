import unittest
from src.dinasore.resources.function_blocks.MES.MQTT_PUBLISHER_V3 import MQTT_PUBLISHER_V3
from unittest.mock import MagicMock
from paho.mqtt.client import Client
from copy import deepcopy

class Test_MQTT_PUBLISHER_V3(unittest.TestCase):
    
    def setUp(self):
        self.publisher = MQTT_PUBLISHER_V3()

        # create mocks
        self.publisher.client.connect = MagicMock()
        self.publisher.client.connect.return_value = None
        self.publisher.client.disconnect = MagicMock()
        self.publisher.client.disconnect.return_value = None
        self.publisher.client.publish = MagicMock()
        self.publisher.client.publish.return_value = None
    
    def tearDown(self):
        del self.publisher
        
    def test_create_publisher(self):
        # assert if client in publisher is not None and of type Client
        self.assertIsNotNone(self.publisher.client)
        self.assertIsInstance(self.publisher.client, Client)

        # assert if total_messages_sent in publisher is 0
        self.assertEqual(self.publisher.total_messages_sent, 0)
            
    def test_schedule_init(self):
        event_name = 'INIT'
        event_value = 1
        topic = 'test_topic'
        host = 'test_host'
        port = 1883
        value_name_1 = 'test_value_name_1'
        value_name_2 = 'test_value_name_2'
        value_name_3 = 'test_value_name_3'
        value_1 = 1
        value_2 = 2.0
        value_3 = 3.0
        
        expected = [event_value, None]
        expected_messages_sent = 0

        actual = self.publisher.schedule(event_name, event_value, topic, host, port,
                                         value_name_1, value_name_2, value_name_3, value_1, value_2, value_3)
        self.assertEqual(expected, actual)
        
        self.publisher.client.connect.assert_called_once_with(host, port)
        self.publisher.client.publish.assert_not_called()
        self.assertEqual(self.publisher.total_messages_sent, expected_messages_sent)

    def test_schedule_init_failure(self):
        event_name = 'INIT'
        event_value = None
        topic = 'test_topic'
        host = 'localhost'
        port = 1883
        value_name_1 = 'value_1'
        value_name_2 = 'value_2'
        value_name_3 = 'value_3'
        value_1 = 1
        value_2 = 2.0
        value_3 = 3.0

        expected_output = [event_value, None]
        expected_messages_sent = 0

        self.publisher.client.connect.side_effect = Exception('Connection error')
  
        output = self.publisher.schedule(event_name, event_value, topic, host, port, value_name_1, value_name_2, value_name_3, value_1, value_2, value_3)
        self.assertEqual(output, expected_output)
        self.publisher.client.connect.assert_called_once_with(host, port)
        self.publisher.client.publish.assert_not_called()
        self.assertEqual(self.publisher.total_messages_sent, expected_messages_sent)

    def test_schedule_run(self):
        event_name = 'RUN'
        event_value = 1
        topic = 'test_topic'
        host = 'test_host'
        port = 1883
        value_name_1 = 'test_value_name_1'
        value_name_2 = 'test_value_name_2'
        value_name_3 = 'test_value_name_3'
        value_1 = 1
        value_2 = 2.0
        value_3 = 3.0
        
        expected = [None, event_value]
        expected_messages_sent = 1

        actual = self.publisher.schedule(event_name, event_value, topic, host, port,
                                         value_name_1, value_name_2, value_name_3, value_1, value_2, value_3)
        self.assertEqual(expected, actual)
        
        self.publisher.client.publish.assert_called_once_with(topic, '{"test_value_name_1": "1", "test_value_name_2": "2.0", "test_value_name_3": "3.0"}')
        self.assertEqual(self.publisher.total_messages_sent, expected_messages_sent)

    def test_schedule_run_failure(self):
        event_name = 'RUN'
        event_value = 1
        topic = 'test_topic'
        host = 'test_host'
        port = 1883
        value_name_1 = 'test_value_name_1'
        value_name_2 = 'test_value_name_2'
        value_name_3 = 'test_value_name_3'
        value_1 = 1
        value_2 = 2.0
        value_3 = 3.0
        
        expected = [event_value, None]
        expected_messages_sent = 0

        self.publisher.client.publish.side_effect = Exception('Connection error')

        actual = self.publisher.schedule(event_name, event_value, topic, host, port,
                                         value_name_1, value_name_2, value_name_3, value_1, value_2, value_3)
        self.assertEqual(expected, actual)
        
        self.publisher.client.publish.assert_called_once_with(topic, '{"test_value_name_1": "1", "test_value_name_2": "2.0", "test_value_name_3": "3.0"}')
        self.assertEqual(self.publisher.total_messages_sent, expected_messages_sent)


    def test_delete_publisher(self):
        # assert if subscriber delete method disconnects the client
        self.publisher.__del__()
        self.publisher.client.disconnect.assert_called_once()