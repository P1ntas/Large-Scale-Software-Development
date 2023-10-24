from threading import Event
from paho.mqtt.client import Client
import json


class SharedResources:

    def __init__(self):
        self.client = None
        self.topic = None
        self.message_payload = None
        self.new_message = Event()

    def connect(self, host, port):
        self.client = Client()

        def on_message(client, userdata, message):
            self.topic = message.topic
            self.message_payload = message.payload
            self.new_message.set()

        self.client.on_message = on_message
        self.client.connect(host, port)
        self.client.loop_start()


class MQTT_SUBSCRIBER_V3:
    resources = SharedResources()

    def __init__(self):
        self.resources.new_message.clear()
        self.stop = Event()

    def schedule(self, event_name, event_value, topic, host, port, value_name_1, value_name_2, value_name_3):
        if event_name == 'INIT':
            try:
                self.resources.connect(host, port)
                self.resources.client.subscribe(topic)
                return [event_value, None, 0, 0.0, 0.0]
            except Exception as e:
                print(f"An error occurred: {e}")
                return [event_value, None, 0, 0.0, 0.0]

        elif event_name == 'READ':
            # wait for new messages
            while not self.stop.is_set():
                self.resources.new_message.wait()

                # checks if is the right topic
                if self.resources.topic == topic and self.resources.message_payload is not None:
                    # process each message
                    msg = self.resources.message_payload.decode('utf-8')
                    payload_json = json.loads(msg)
                    value_1 = int(payload_json[value_name_1])
                    value_2 = float(payload_json[value_name_2])
                    value_3 = float(payload_json[value_name_3])
                    # otherwise clears the new message event
                    self.resources.new_message.clear()
                    return [None, event_value, value_1, value_2, value_3]

    def __del__(self):
        self.stop.set()
        self.resources.new_message.clear()
        self.resources.client.disconnect()
