import psycopg2
import random
import time
import logging
from prometheus_client import CollectorRegistry, Gauge, generate_latest
from flask import Flask, Response
from threading import Thread

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)

def db_connection():
    max_retries = 10
    retry_delay = 5  # seconds

    for attempt in range(1, max_retries + 1):
        logger.info(f"Attempt {attempt}: Connecting to the database")
        try:
            connection = psycopg2.connect(
                dbname='postgres',
                user='postgres',
                password='postgres',
                host='postgres',
                port='5432'
            )
            logger.info("Successfully connected to the database")
            return connection
        except Exception as e:
            if attempt < max_retries:
                logger.warning(f"An error occurred: {e}. Retrying in {retry_delay} seconds...")
                time.sleep(retry_delay)
            else:
                logger.error(f"Max retries reached. An error occurred: {e}")
                raise e

def fetch_sensors_data():
    connection = None
    cursor = None
    try:
        connection = db_connection()

        if not connection:
            raise Exception("No connection to database")

        cursor = connection.cursor()
        logger.info("Fetching sensors data...")
        cursor.execute("""
            select s.id, sm.min_value, sm.max_value from sensor s
            inner join sensor_model sm on s.sensor_model_id = sm.id
        """)
        return cursor.fetchall()
    except Exception as e:
        logger.error(f"An error occurred: {e}")
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()

registry = CollectorRegistry()
SENSOR_VALUE = Gauge('sensor_value', 'Value of the sensor', ['sensor_id'], registry=registry)

@app.route('/metrics', methods=['GET'])
def metrics():
    return Response(generate_latest(registry), content_type='text/plain; version=0.0.4; charset=utf-8')

def generate_data():
    data = fetch_sensors_data()

    if not data:
        raise Exception("No data available")
    
    data_length = len(data) + 1 # +1 to avoid division by zero, even though it should never happen

    logger.info("Starting data generation")
    
    while True:
        for sensor_id, min_value, max_value in data:
            generated_value = random.uniform(min_value, max_value)
            SENSOR_VALUE.labels(sensor_id=str(sensor_id)).set(generated_value)
            time.sleep(1/data_length)
        time.sleep(4)

if __name__ == '__main__':
    thread = Thread(target=generate_data)
    thread.start()

    app.run(host='0.0.0.0', port=8000)