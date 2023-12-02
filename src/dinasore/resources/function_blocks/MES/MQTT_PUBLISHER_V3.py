from paho.mqtt.client import Client
import json


class MQTT_PUBLISHER_V3:

    def __init__(self):
        self.client = Client()
        self.total_messages_sent = 0

    def schedule(
            self,
            event_name,
            event_value,
            topic,
            host,
            port,
            value_name_1,
            value_name_2,
            value_name_3,
            value_1,
            value_2,
            value_3):
        if event_name == 'INIT':
            # connects to the broker
            try:
                print(f"Connecting to the broker...")
                self.client.connect(host, port)
                print(f"Connected to the broker {host}:{port}")
                return [event_value, None]
            except Exception as e:
                print(f"An error occurred: {e}")
                return [event_value, None]

        elif event_name == 'RUN':
            try:
                message_dict = {value_name_1: str(value_1),
                                value_name_2: str(value_2),
                                value_name_3: str(value_3)}
                message = json.dumps(message_dict)
                self.client.publish(topic, message)
                self.total_messages_sent += 1
                return [None, event_value]

            except Exception as e:
                print(f"An error occurred: {e}")
                return [event_value, None]

    def __del__(self):
        self.client.disconnect()
