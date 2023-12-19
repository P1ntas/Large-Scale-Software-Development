import random
from datetime import datetime, timedelta

def data_generator():
    facilities = ['Continental', 'Bosch', 'Volkswagen Autoeuropa']
    tags = ['CONT', 'BOS', 'VWAE']
    manufacturers = ['Festo', 'Siemens', 'Schneider', 'ABB', 'Rockwell']
    locations = ['PT01 Porto', 'PT02 Lisbon', 'PT03 Braga']
    coordinates = {
        'PT01 Porto': [41.1496, -8.6109],
        'PT02 Lisbon':[38.7223, -9.1393],
        'PT03 Braga': [41.5454, -8.4265]
    }

    system_model_names = ['MPS 203 I4.0', 'CP Lab', 'CP Factory'] # taken example from https://www.festo.com/net/SupportPortal/Files/492858/Poster_DINA2_I4o_Solutions_205x292_EN_screen.pdf
    system_model_types = {
        'MPS 203 I4.0': 'Basic',
        'CP Lab': 'Advanced',
        'CP Factory': 'Expert'
    }

    expansion_model_names = ['3D Printer', 'Conveyor Belt', 'Robot Arm', 'Pneumatic Gripper', 'Vacuum Gripper', 'RFID', 'PLC', 'HMI']
    expansion_model_types = {
        '3D Printer': 'Module',
        'Conveyor Belt': 'Module',
        'Robot Arm': 'Module',
        'Pneumatic Gripper': 'Component',
        'Vacuum Gripper': 'Component',
        'RFID': 'Station',
        'PLC': 'Station',
        'HMI': 'Station'
    }

    sensor_model_names = ['Thermocouple', 'Rotameter', 'Strain Gauge']
    sensor_model_types = {
        'Thermocouple': 'Temperature',
        'Rotameter': 'Flow',
        'Strain Gauge': 'Pressure'
    }
    sensor_model_values = {
        'Thermocouple': [random.uniform(10, 50), random.uniform(51, 100)],
        'Rotameter': [random.uniform(10, 50), random.uniform(51, 100)],
        'Strain Gauge': [random.uniform(10, 50), random.uniform(51, 100)]
    }
    task_names= ['Uniformity Testing', 'X-ray Inspection', 'Balancing', 'Curing Process', 'Rubber Compound Extrusion', 'Temperature and Pressure Calibration',
                 'Material Feeding Control', 'Quality Check at Extrusion Point', 'Inner Liner Material Feeding', 'Adhesive Application', 'Liner Thickness Control',
                  'Wire Spool Loading', 'Bead Winding Process', 'Bead Diameter Verification', 'Cutting and Shaping', 'Quality Inspection at Bead Assembly', 'Conveyor Belt Alignment',
                   'Pallet Loading and Unloading', 'Material Transport to Different Stations', 'Gripper Calibration', 'Robot Arm Lubrication' ]


    # Give a higher probability to the 'Working'/'Online' status
    status_options = ['Offline', 'Working', 'Working', 'Working', 'Maintenance Required', 'Online', 'Online', 'Online']

    sql_file_path = "data/sample_data.sql"

    try:
        with open(sql_file_path, "w") as f:   

            # Writing systems models
            for i in range(system_model_names.__len__()):
                system_model_name = system_model_names[i]
                manufacturer = random.choice(manufacturers)
                system_type = system_model_types[system_model_name]
                f.write(f"INSERT INTO system_model (name, manufacturer, type) VALUES ('{system_model_name}', '{manufacturer}', '{system_type}');\n")

            # Writing expansion models
            for i in range(expansion_model_names.__len__()):
                expansion_model_name = expansion_model_names[i]
                manufacturer = random.choice(manufacturers)
                expansion_type = expansion_model_types[expansion_model_name]
                f.write(f"INSERT INTO expansion_model (name, manufacturer, type) VALUES ('{expansion_model_name}', '{manufacturer}', '{expansion_type}');\n")

            # Writing sensor models
            for i in range(sensor_model_names.__len__()):
                sensor_model_name = sensor_model_names[i]
                manufacturer = random.choice(manufacturers)
                sensor_type = sensor_model_types[sensor_model_name]
                sensor_value = sensor_model_values[sensor_model_name]
                f.write(f"INSERT INTO sensor_model (name, manufacturer, type, min_value, max_value) VALUES ('{sensor_model_name}', '{manufacturer}', '{sensor_type}', {sensor_value[0]}, {sensor_value[1]});\n")

            current_system_id = 0
            current_expansion_id = 0

            # Writing factories
            for i in range(facilities.__len__()):
                factory_name = facilities[i]
                tag = tags[i]
                location = locations[i]
                latitude = coordinates[location][0]
                longitude = coordinates[location][1]
                f.write(f"INSERT INTO factory (name, tag, location, longitude, latitude) VALUES ('{factory_name}', '{tag}', '{location}', {longitude}, {latitude});\n")    

                # Writing systems for each factory
                num_systems = random.randint(5, 10)

                for j in range(num_systems):
                    current_system_id += 1
                    system_model_id = random.randint(1, 3)
                    sys_status = random.choice(status_options)
                    f.write(f"INSERT INTO system (factory_id, system_model_id, status) VALUES ({i + 1}, {system_model_id}, '{sys_status}');\n")

                    # Writing expansions for each system
                    num_expansions = random.randint(2, 5)
                    for k in range(num_expansions):
                        current_expansion_id += 1
                        expansion_model_id = random.randint(1, 8)
                        exp_status = random.choice(status_options)
                        f.write(f"INSERT INTO expansion (system_id, expansion_model_id, status) VALUES ({current_system_id}, {expansion_model_id}, '{exp_status}');\n")

                        # Writing sensors for each expansion
                        num_sensors = random.randint(1, 2)
                        for l in range(num_sensors):
                            sensor_model_id = random.randint(1, 3)
                            sens_status = random.choice(status_options)
                            f.write(f"INSERT INTO sensor (expansion_id, sensor_model_id, status) VALUES ({current_expansion_id}, {sensor_model_id}, '{sens_status}');\n")

                    # Writing tasks
                    def_task_name = ''
                    task_duration = {}
                    for m in range(2):
                        task_name = random.choice([tsk_name for tsk_name in task_names if tsk_name != def_task_name])
                        def_task_name = task_name
                        duration = random.choice(['10 min','20 min','30 min','40 min','50 min' , '60 min'])
                        task_duration[m] = duration
                        energetic_costs = random.randint(40,70)
                        f.write(f"INSERT INTO task (system_id, name, duration, energetic_costs) VALUES ({current_system_id}, '{task_name}', '{duration}', {energetic_costs});\n")

                    start_date = datetime.now() - timedelta(hours=20)
                    mins_in_a_day = 24 * 60
                    n = 0

                    while n < mins_in_a_day:
                        # select duration of a task
                        choices = {
                            0: 3, # 1/3 chance to select task 1
                            1: 3, # 1/3 chance to select task 2
                            2: 3  # 1/3 chance to select null
                        }
                        random_task = random.choices(list(choices.keys()), weights=choices.values())[0]
                        
                        if random_task != 2:
                            task_id = 2 * current_system_id + random_task - 1
                            duration_str = task_duration[random_task]
                        else:
                            task_id = None
                            duration_str = random.choice(['10 min', '20 min', '30 min', '40 min', '50 min', '60 min'])

                        duration_minutes = int(duration_str.split()[0])

                        timestamp = start_date + timedelta(minutes=n)

                        if task_id:
                            # Write to file
                            f.write(f"INSERT INTO task_timeseries (task_id, timestamp, system_id) VALUES ({task_id}, '{timestamp}', {current_system_id});\n")
                        else:
                            # Write to file
                            f.write(f"INSERT INTO task_timeseries (timestamp, system_id) VALUES ('{timestamp}', {current_system_id});\n")
                        # Increment n by the duration in minutes
                        n += duration_minutes

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        print("Data generated successfully")