import psycopg2
import pandas as pd


def insert_into_sql_table():
    df = pd.read_csv("country_weather.csv")
    print(df)

    try:
        connection = psycopg2.connect(host="postgres", database="airflow", user="airflow", password="airflow",
                                      port='5432')
        cur = connection.cursor()

        query = "Insert INTO state_weather (STATE, DESCRIPTION, TEMPERATURE, FEELS_LIKE_TEMPERATURE, MIN_TEMP, " \
                "MAX_TEMP, HUMIDITY,CLOUDS) values (%s,%s,%s,%s,%s,%s,%s,%s)"

        for index, row in df.iterrows():
            cur.execute(query, (
                row['State'], row['Description'], row['Temperature'], row['Feels_Like_Temperature']
                , row['Min_Temp'], row['Max_Temp'], row['Humidity'], row['Clouds']))

        connection.commit()

        print("Inserted into table successfully")

    except:
        print("Could not insert into database. Unknown error occurred.")

    finally:
        if connection is not None:
            connection.commit()
            connection.close()
