from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta
from country_weather_csv import create_new_csv
from create_weather_table import create_sql_table
from insert_into_table import insert_into_sql_table

default_args = {
    "owner": "Poulomi",
    "depends_on_past": False,
    "start_date": datetime(2022, 3, 14),
    "email": ["airflow@airflow.com"],
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=5)
}

dag = DAG("Dag", default_args=default_args, schedule_interval="0 6 * * *")

t1 = PythonOperator(task_id='create_csv', python_callable=create_new_csv, dag=dag)
t2 = PythonOperator(task_id='create_sql_table', python_callable=create_sql_table, dag=dag)
t3 = PythonOperator(task_id='insert_sql_table', python_callable=insert_into_sql_table, dag=dag)

t1 >> t2 >> t3