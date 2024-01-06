from airflow import DAG
from airflow.operators.empty import EmptyOperator
from datetime import datetime
from airflow.decorators import task_group

@task_group(group_id='subdag')
def subdag_taskgroup():
    inner_task1 = EmptyOperator(task_id="task1_subdag")
    inner_task2 = EmptyOperator(task_id="task2_subdag")
    inner_task3 = EmptyOperator(task_id="task3_subdag")
    inner_task4 = EmptyOperator(task_id="task4_subdag")
    inner_task1_2 = EmptyOperator(task_id="task1_2_subdag")
    inner_task2_2 = EmptyOperator(task_id="task2_2_subdag")
    inner_task3_2 = EmptyOperator(task_id="task3_2_subdag")
    inner_task4_2 = EmptyOperator(task_id="task4_2_subdag")

    inner_task1 >> inner_task1_2
    inner_task2 >> inner_task2_2
    inner_task3 >> inner_task3_2
    inner_task4 >> inner_task4_2

with DAG("09-taskgroup-example", start_date=datetime(2024,1,4), schedule_interval="@daily") as dag:
    # Define tasks in the main DAG
    task1 = EmptyOperator(task_id="task1_group1")
    task2 = EmptyOperator(task_id="task2_group1")

    subdag_group = subdag_taskgroup()

    task3 = EmptyOperator(task_id="task3")

    #Set task dependencies
    task1 >> task2 >> subdag_group >> task3