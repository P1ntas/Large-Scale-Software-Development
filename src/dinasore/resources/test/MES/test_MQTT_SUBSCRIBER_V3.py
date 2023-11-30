import unittest
from dinasore.resources.function_blocks.MES.MQTT_SUBSCRIBER_V3 import MQTT_SUBSCRIBER_V3
from dinasore.resources.function_blocks.MES.MQTT_SUBSCRIBER_V3 import SharedResources
from threading import Event
from unittest.mock import MagicMock

class Test_MQTT_SUBSCRIBER_V3(unittest.TestCase):
    def setUp(self):
        self.subscriber = MQTT_SUBSCRIBER_V3()
        
        client = MagicMock()
        client.subscribe = MagicMock()
        client.subscribe.return_value = None
        client.disconnect = MagicMock()
        client.disconnect.return_value = None

        connect = MagicMock()
        connect.return_value = None

        self.subscriber.resources.client = client
        self.subscriber.resources.connect = connect
    
    def tearDown(self):
        del self.subscriber

    def test_create_subscriber(self):
        self.assertIsNotNone(self.subscriber.resources)
        self.assertIsInstance(self.subscriber.resources, SharedResources)

        self.assertIsNotNone(self.subscriber.stop)
        self.assertIsInstance(self.subscriber.stop, Event)

        self.assertEqual(self.subscriber.resources.new_message.is_set(), False)

    def test_schedule_init(self):
        event_name = 'INIT'
        event_value = 1
        topic = 'test_topic'
        host = 'test_host'
        port = 1883
        value_name_1 = 'test_value_name_1'
        value_name_2 = 'test_value_name_2'
        value_name_3 = 'test_value_name_3'
        expected = [event_value, None, 0, 0.0, 0.0]

        actual = self.subscriber.schedule(event_name, event_value, topic, host, port, value_name_1, value_name_2, value_name_3)
        self.assertEqual(expected, actual)
        self.subscriber.resources.connect.assert_called_once_with(host, port)
        self.subscriber.resources.client.subscribe.assert_called_once_with(topic)

    def test_schedule_init_failure(self):
        event_name = 'INIT'
        event_value = None
        topic = 'test_topic'
        host = 'localhost'
        port = 1883
        value_name_1 = 'value_1'
        value_name_2 = 'value_2'
        value_name_3 = 'value_3'

        expected_output = [event_value, None, 0, 0.0, 0.0]


        self.subscriber.resources.connect.side_effect = Exception('Connection error')
 
        output = self.subscriber.schedule(event_name, event_value, topic, host, port, value_name_1, value_name_2, value_name_3)
        self.assertEqual(output, expected_output)
        self.subscriber.resources.connect.assert_called_once_with(host, port)

    def test_schedule_read(self):
        event_name = 'READ'
        event_value = None
        topic = 'test_topic'
        host = 'localhost'
        port = 1883
        value_name_1 = 'value_1'
        value_name_2 = 'value_2'
        value_name_3 = 'value_3'

        expected_output = [None, event_value, 1, 2.0, 3.0]

        new_message = MagicMock()
        new_message.wait = MagicMock()
        new_message.wait.return_value = True
        new_message.clear = MagicMock()
        new_message.clear.return_value = None

        self.subscriber.resources.new_message = new_message
        self.subscriber.resources.topic = topic
        self.subscriber.resources.message_payload = '{"value_1": 1, "value_2": 2.0, "value_3": 3.0}'.encode('utf-8')

        output = self.subscriber.schedule(event_name, event_value, topic, host, port, value_name_1, value_name_2, value_name_3)
        self.assertEqual(output, expected_output)
        self.subscriber.resources.new_message.clear.assert_called_once()

    def test_delete_subscriber(self):
        self.subscriber.__del__()
        self.assertEqual(self.subscriber.stop.is_set(), True)
        self.assertEqual(self.subscriber.resources.new_message.is_set(), False)
        self.subscriber.resources.client.disconnect.assert_called_once()
        
