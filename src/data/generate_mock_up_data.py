import pandas as pd
import numpy as np
import random
import datetime

# Load existing data
sensor_model_df = pd.read_csv('csv_data/sensor_model.csv')
sensor_df = pd.read_csv('csv_data/sensor.csv')
expansion_df = pd.read_csv('csv_data/expansion.csv')

# Create a list to store the mock sensor data
mock_data_list = []

# Generate mock sensor data
start_date = datetime.datetime(2023, 1, 1)
end_date = datetime.datetime(2023, 12, 31)
time_range = [start_date + datetime.timedelta(minutes=i) for i in range(int((end_date - start_date).total_seconds() / 3600))]

for sensor_id in sensor_df['id']:
    for timestamp in time_range:
        # Generate a random temperature within the sensor's min and max values
        sensor_row = sensor_df[sensor_df['id'] == sensor_id].iloc[0]
        min_value = sensor_model_df[sensor_model_df['id'] == sensor_row['sensor_model_id']]['min_value'].iloc[0]
        max_value = sensor_model_df[sensor_model_df['id'] == sensor_row['sensor_model_id']]['max_value'].iloc[0]
        temperature = random.uniform(min_value, max_value)
        
        # Simulate some sensors being in a failed state
        if random.random() < 0.1:
            status = 'Failed'
        else:
            status = 'Normal'
        
        mock_data_list.append({'timestamp': timestamp, 'sensor_id': sensor_id, 'temperature': temperature, 'status': status})

# Convert the list of dictionaries to a DataFrame
mock_data = pd.DataFrame(mock_data_list)

# Save the mock sensor data to a CSV file
mock_data.to_csv('csv_data/mock_sensor_data.csv', index=False)

