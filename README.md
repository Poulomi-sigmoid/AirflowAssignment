This project contains the solution to the Airflow Assignment.

The following are the questions and name of the corresponding files containing the solutions :

Subscribe to https://rapidapi.com/community/api/open-weather-map/

Use the docker container to create airflow and postgres instances.

1. Create the first task to use endpoint /Current Weather Data for at least 10 states of India and fill up the csv file with details of 
    State, Description, Temperature, Feels Like Temperature, Min Temperature, Max Temperature, Humidity, Clouds. - country_weather_csv.py
2. Create a second task to create a postgres table “Weather” that would have columns same as the csv file. -  create_weather_table.py
3. Create a third task that should fill the columns of the table while reading the data from the csv file. - insert_into_table.py
4. Schedule the DAG in AirFlow to run every day at 6:00 am and update the daily weather detail in csv as well as the table. - Dag.py
