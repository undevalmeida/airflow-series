from airflow import DAG
from airflow.operators.empty import EmptyOperator
from datetime import datetime

# Não tão legal
"""
dag = DAG(dag_id='01-our_first_dag', start_date=datetime(2023,12,18))

task1 = EmptyOperator(task_id='extract',dag=dag)
task2 = EmptyOperator(task_id='transform',dag=dag)
task3 = EmptyOperator(task_id='load',dag=dag)

task1 >> task2 >> task3

"""

# Boa

with DAG(
    dag_id='01-our_first_dag'
    , start_date=datetime(2023,12,18)
    , schedule='@daily') as dag:

    task1 = EmptyOperator(task_id='extract',dag=dag)
    task2 = EmptyOperator(task_id='transform',dag=dag)
    task3 = EmptyOperator(task_id='load',dag=dag)

    task1 >> task2 >> task3



# ----- || --------
    
# Muito legal
"""
from airflow.decorators.python import dag, task

@dag(
        start_date
)
def our_first_dag():
"""