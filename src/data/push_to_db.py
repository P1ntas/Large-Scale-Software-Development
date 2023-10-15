import psycopg2

def db_connection():
    try:
        return psycopg2.connect(
            dbname='postgres',
            user='postgres',
            password='postgres',
            host='localhost',
            port='5432'
        )
    except Exception as e:
        print(f"An error occurred: {e}")

def create_db():
    try:
        with open("data/create.sql", "r") as f:
            print("Creating database...")
            sql = f.read()
            if sql == "":
                raise Exception("No SQL to execute")
            connection = db_connection()
            if connection is None:
                raise Exception("No connection to database")
            cursor = connection.cursor()
            cursor.execute(sql)
            connection.commit()
            cursor.close()
            connection.close()
            print("Database created successfully")
    except Exception as e:
        print(f"An error occurred: {e}")
    
def push_data_to_db():
    try:
        with open("data/sample_data.sql", "r") as f:
            print("Pushing data to database...")
            sql = f.read()
            if sql == "":
                raise Exception("No data to push")
            connection = db_connection()
            cursor = connection.cursor()
            cursor.execute(sql)
            connection.commit()
            cursor.close()
            connection.close()
            print("Data pushed successfully")
    except Exception as e:
        print(f"An error occurred: {e}")