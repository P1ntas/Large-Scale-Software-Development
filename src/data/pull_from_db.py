import csv
import psycopg2
import os

db_params = {
    'host': 'localhost',
    'port': 5432, 
    'database': 'postgres',
    'user': 'postgres',
    'password': 'postgres'
}

table_names = [
    'expansion',
    'expansion_model',
    'factory',
    'sensor',
    'sensor_model',
    'system',
    'system_model'
]

conn = psycopg2.connect(**db_params)
cursor = conn.cursor()
output_dir = 'csv_data'

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

for table_name in table_names:
    select_query = f"SELECT * FROM {table_name};"

    cursor.execute(select_query)
    rows = cursor.fetchall()

    csv_file_path = os.path.join(output_dir, f'{table_name}.csv')
    with open(csv_file_path, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow([desc[0] for desc in cursor.description])
        csv_writer.writerows(rows)

    print(f"Data from '{table_name}' has been exported to '{csv_file_path}'")

cursor.close()
conn.close()
