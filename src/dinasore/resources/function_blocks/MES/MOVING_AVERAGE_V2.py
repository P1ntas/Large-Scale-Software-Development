class MOVING_AVERAGE_V2:

    def __init__(self):
        self.values_dict = {}  # Use a dictionary to store values for each sensor_id

    def schedule(self, event_name, event_value, window, sensor_id, value):
        if event_name == 'INIT':
            self.values_dict[sensor_id] = []  # Initialize an empty list for the sensor_id
            return [event_value, None, 0, 0]

        elif event_name == 'RUN':
            if sensor_id not in self.values_dict:
                self.values_dict[sensor_id] = []  # Initialize an empty list for the sensor_id if it doesn't exist
            # Appends the value to the list for the corresponding sensor_id
            self.values_dict[sensor_id].append(value)
            values_list = self.values_dict[sensor_id]
            # Checks the size of the list
            if len(values_list) == window:
                # Calculate the moving average for the sensor_id
                moving_average = sum(values_list) / window
                # Removes the oldest value
                values_list.pop(0)
                # Returns the moving average value for the sensor_id
                return [None, event_value, sensor_id, moving_average]
            else:
                # The list doesn't have the correct size for the sensor_id
                print(f"Sensor {sensor_id} doesn't have enough values: {len(values_list)}/{window}")
                return [None, None, 0, 0]
