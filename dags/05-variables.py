from airflow import DAG
from airflow.models import Variable
from airflow.operators.python import PythonOperator
from datetime import datetime

dumy_variable = Variable.get(key='dummy_variable')

def dummy():
    print(f"`{dumy_variable}")

""" key = 'value' Essa variável é definida dentro do apache airflow: admin > variable > '+' """

#s3_path = Variable.get(key='key')

with DAG(
    dag_id='05-variables'
    , start_date=datetime(2023,12,26)
    , schedule=None
    ) as dag:

    task1 = PythonOperator(python_callable=dummy, task_id='task1')

    task2 = PythonOperator(python_callable=dummy, task_id='task2')

    task3 = PythonOperator(python_callable=dummy, task_id='task3')
