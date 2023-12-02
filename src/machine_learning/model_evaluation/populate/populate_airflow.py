import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Settings
num_entries = 1000
start_date = datetime(2023, 1, 1)
sensor_id = "AF101"
sensor_model = "AF-X9"
error_codes = ["NA", "E101", "E102", "E103"]
statuses = ["Working", "Needs Maintenance", "Down"]

# Generate data
data = []
for i in range(num_entries):
    date = start_date + timedelta(hours=i)
    airflow = np.random.normal(300, 50)  # Average 300 CFM, with some variance
    status = np.random.choice(statuses, p=[0.8, 0.15, 0.05])
    last_maintenance_date = date - timedelta(days=np.random.randint(30, 180))
    ambient_temp = np.random.uniform(18, 25)
    ambient_pressure = np.random.uniform(1010, 1020)
    last_calibration_date = date - timedelta(days=np.random.randint(30, 180))
    error_code = np.random.choice(error_codes, p=[0.9, 0.05, 0.03, 0.02])

    data.append([date, sensor_id, airflow, status, last_maintenance_date, 
                 ambient_temp, ambient_pressure, sensor_model, 
                 last_calibration_date, error_code])

# Create DataFrame and save to CSV
df = pd.DataFrame(data, columns=["Timestamp", "Sensor ID", "Airflow Reading (CFM)", 
                                 "Operational Status", "Last Maintenance Date", 
                                 "Ambient Temperature", "Ambient Pressure", 
                                 "Sensor Model", "Last Calibration Date", 
                                 "Error Code"])
df.to_csv("../data/airflow_sensor_data.csv", index=False)
