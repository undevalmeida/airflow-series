from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def function_example():
    print("Testando minha primeira função python")


with DAG(
    dag_id='02-python_operator_example'
    , start_date=datetime(2023,12,19), schedule=None) as dag:

    task1 = PythonOperator(
        task_id = 'first_function',
        python_callable = function_example
    )