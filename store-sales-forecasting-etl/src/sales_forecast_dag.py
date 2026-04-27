from datetime import datetime

from airflow import DAG
from airflow.operators.python import PythonOperator


def extract_data():
    # TODO: загрузить исходные файлы Kaggle из data/raw
    pass


def transform_data():
    # TODO: очистить данные и подготовить признаки
    pass


def train_forecast_model():
    # TODO: обучить baseline и ML-модель прогноза
    pass


def validate_outputs():
    # TODO: проверить качество данных и адекватность прогноза
    pass


with DAG(
    dag_id="store_sales_forecasting_pipeline",
    start_date=datetime(2026, 1, 1),
    schedule="@weekly",
    catchup=False,
    tags=["portfolio", "forecasting", "etl"],
) as dag:
    extract = PythonOperator(task_id="extract_data", python_callable=extract_data)
    transform = PythonOperator(task_id="transform_data", python_callable=transform_data)
    train = PythonOperator(task_id="train_forecast_model", python_callable=train_forecast_model)
    validate = PythonOperator(task_id="validate_outputs", python_callable=validate_outputs)

    extract >> transform >> train >> validate
