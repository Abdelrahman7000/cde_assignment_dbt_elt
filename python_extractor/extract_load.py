import requests 
from sqlalchemy import *
import pandas as pd
import time


def extract_data():
    res=requests.get('https://randomuser.me/api/').json()['results']
    df = pd.json_normalize(res)
    return df

def load_data(df):
    # Connection string uses the service name 'postgres_db' as the host
    DB_HOST = 'postgres_db'
    DB_PORT = 5432
    DB_NAME = 'staging_db'
    DB_USER = 'postgres'
    DB_PASS = 'password' 

    engine = create_engine(f'postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}')

    print("Connecting to Postgres...")
    # Load the DataFrame into a table named 'raw_data'
    df.to_sql('users', engine, if_exists='append', index=False)
    print("Data successfully loaded into 'raw_data' table.")


if __name__ == "__main__":
    # retry the process till the database becomes ready
    for i in range(10):
        try:
            df=extract_data()
            load_data(df)
            break
        except Exception as e:
            print(f"Database not ready yet. Retrying in 5s... ({i+1}/10)")
            time.sleep(5)
    else:
        print("Failed to connect to the database after multiple retries.")