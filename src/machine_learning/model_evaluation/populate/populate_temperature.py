import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Settings for temperature sensor data generation
num_entries = 1000
start_date = datetime(2023, 1, 1)
sensor_id = "TS313"
sensor_model = "TS-T2"
error_codes = ["NA", "E301", "E302", "E303"]
statuses = ["Working", "Needs Maintenance", "Down"]

# Generate temperature sensor data
data = []
for i in range(num_entries):
    date = start_date + timedelta(hours=i)
    temperature = np.random.normal(22, 2)  # Average 22°C, with variance
    status = np.random.choice(statuses, p=[0.8, 0.15, 0.05])
    last_maintenance_date = date - timedelta(days=np.random.randint(30, 180))
    ambient_humidity = np.random.uniform(30, 70)
    heat_source_proximity = np.random.choice(["Near", "Medium", "Far"], p=[0.2, 0.5, 0.3])
    last_calibration_date = date - timedelta(days=np.random.randint(30, 180))
    error_code = np.random.choice(error_codes, p=[0.9, 0.03, 0.04, 0.03])

    data.append([date, sensor_id, temperature, status, last_maintenance_date, 
                 ambient_humidity, heat_source_proximity, sensor_model, 
                 last_calibration_date, error_code])

# Create DataFrame and save to CSV
df = pd.DataFrame(data, columns=["Timestamp", "Sensor ID", "Temperature Reading (°C)", 
                                 "Operational Status", "Last Maintenance Date", 
                                 "Ambient Humidity", "Heat Source Proximity", 
                                 "Sensor Model", "Last Calibration Date", 
                                 "Error Code"])
df.to_csv("../data/temperature_sensor_data.csv", index=False)
