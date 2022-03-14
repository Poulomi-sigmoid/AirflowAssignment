import psycopg2
import pandas as pd


def create_sql_table():

    create_query = """CREATE TABLE state_weather(
        STATE VARCHAR(30),
        DESCRIPTION varchar(30),
        TEMPERATURE decimal,
        FEELS_LIKE_TEMPERATURE decimal,
        MIN_TEMP decimal,
        MAX_TEMP decimal,
        HUMIDITY numeric,
        CLOUDS numeric)"""

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
