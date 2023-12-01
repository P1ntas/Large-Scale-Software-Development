import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Settings for pressure sensor data generation
num_entries = 1000
start_date = datetime(2023, 1, 1)
sensor_id = "PS205"
sensor_model = "PS-L4"
error_codes = ["NA", "E201", "E202", "E203"]
statuses = ["Working", "Needs Maintenance", "Down"]

# Generate pressure sensor data
data = []
for i in range(num_entries):
    date = start_date + timedelta(hours=i)
    pressure = np.random.normal(105000, 5000)  # Average 105000 Pa, with variance
    status = np.random.choice(statuses, p=[0.85, 0.1, 0.05])
    last_maintenance_date = date - timedelta(days=np.random.randint(30, 180))
    ambient_temp = np.random.uniform(18, 25)
    vibration_level = np.random.choice(["Low", "Medium", "High"], p=[0.6, 0.3, 0.1])
    last_calibration_date = date - timedelta(days=np.random.randint(30, 180))
    error_code = np.random.choice(error_codes, p=[0.9, 0.03, 0.04, 0.03])

    data.append([date, sensor_id, pressure, status, last_maintenance_date, 
                 ambient_temp, vibration_level, sensor_model, 
                 last_calibration_date, error_code])

# Create DataFrame and save to CSV
df = pd.DataFrame(data, columns=["Timestamp", "Sensor ID", "Pressure Reading (Pa)", 
                                 "Operational Status", "Last Maintenance Date", 
                                 "Ambient Temperature", "Vibration Level", 
                                 "Sensor Model", "Last Calibration Date", 
                                 "Error Code"])
df.to_csv("../data/pressure_sensor_data.csv", index=False)
