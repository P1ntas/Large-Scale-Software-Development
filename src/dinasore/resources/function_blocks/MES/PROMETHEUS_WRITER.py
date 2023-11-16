from prometheus_client import CollectorRegistry, Gauge, push_to_gateway


class PROMETHEUS_WRITER:

    def __init__(self):
        self.client = None

    def schedule(self, event_name, event_value,
                 host, port,
                 value_name_1, value_name_2, value_name_2_descr, value_name_3, value_name_3_descr, job_name,
                 value_1, value_2, value_3):
        if event_name == 'INIT':
            print('Setting up prometheus db')
            try:
                self.registry = CollectorRegistry()

                self.SENSOR_VALUE = Gauge(value_name_2, value_name_2_descr, [
                                          value_name_1], registry=self.registry)
                self.MOVING_AVERAGE = Gauge(value_name_3, value_name_3_descr, [
                                            value_name_1], registry=self.registry)
                self.JOB_NAME = job_name
                self.PUSHGATEWAY_ADDRESS = f"{host}:{port}"
                print('Set up prometheus db sucessfully')
            except Exception as e:
                print(f"An error occurred: {e}")

            return [event_value, None]

        elif event_name == 'RUN':
            try:
                self.SENSOR_VALUE.labels(
                    **{value_name_1: str(value_1)}).set(value_2)
                self.MOVING_AVERAGE.labels(
                    **{value_name_1: str(value_1)}).set(value_3)
                push_to_gateway(self.PUSHGATEWAY_ADDRESS,
                                job=self.JOB_NAME, registry=self.registry)
            except Exception as e:
                print(f"Failed to push metrics: {e}")

            return [None, event_value]
