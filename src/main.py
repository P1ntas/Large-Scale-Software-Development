from data.generator import data_generator
from data.push_to_db import create_db, push_data_to_db

if __name__ == "__main__":
    data_generator()
    try:
        create_db()
        push_data_to_db()
    except Exception as e:
        print(e)