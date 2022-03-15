import psycopg2
import pandas as pd


def create_sql_table():

    create_query = """CREATE TABLE state_weather(
        STATE VARCHAR(30),
        DESCRIPTION VARCHAR(30),
        TEMPERATURE DECIMAL,
        FEELS_LIKE_TEMPERATURE DECIMAL,
        MIN_TEMP DECIMAL,
        MAX_TEMP DECIMAL,
        HUMIDITY NUMERIC,
        CLOUDS NUMERIC)"""

    df = pd.read_csv("country_weather.csv")
    print(df)

    try:
        connection = psycopg2.connect(host="postgres", database="airflow", user="airflow", password="airflow",
                                      port='5432')

        print("Database successfully connected.")
        cur = connection.cursor()
        print("Cursor defined")
        cur.execute(create_query)
        print("Successfully created table.")

    except:
        print("Could not create table. Unknown error occurred")

    finally:
        if connection is not None:
            connection.commit()
            connection.close()
