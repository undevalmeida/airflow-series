from airflow import DAG
from airflow.operators.empty import EmptyOperator
from datetime import datetime

with DAG(
    dag_id='03-blackfilling'
    , start_date=datetime(2023,12,15)
    , schedule = '@daily'
    , catchup=False # Não faz o processo de backfilling
    ) as dag:
    
    task1 = EmptyOperator(task_id='first_task')
    task2 = EmptyOperator(task_id='second_task')
    task3 = EmptyOperator(task_id='third_task')

    task1 >> [task2, task3] # task 2 e 3 depende da execução da task1

