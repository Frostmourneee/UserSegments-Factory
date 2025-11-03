from airflow import DAG
from airflow.providers.standard.operators.python import PythonOperator
from datetime import datetime, timedelta

from data_generator import generate_data

default_args = {
    'owner': 'airflow',
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
    'data_generation',
    default_args=default_args,
    description="Автоматический DAG для добавлении данных в БД",
    start_date=datetime(2024, 1, 1),
    schedule=timedelta(minutes=1),
    catchup=False,
    tags=["data", "PostgreSQL"],
    is_paused_upon_creation=False,
) as dag:

    generate_data_task = PythonOperator(
        task_id='generate_test_data',
        python_callable=generate_data,
    )