from airflow import DAG
from airflow.operators.empty import EmptyOperator
from airflow.operators.subdag import SubDagOperator
from datetime import datetime

def subdag(parent_dag_name, child_dag_name, args):
    """ 
    Define a subdag with a single task. 
    """
    subdag = DAG(
        dag_id=f"{parent_dag_name}.{child_dag_name}",
        default_args=args,
        schedule=None,
        start_date=datetime(2024-1-4)
    )

    task1 = EmptyOperator(task_id="task_subdag", dag=subdag)
    task2 = EmptyOperator(task_id="task_subdag", dag=subdag)
    task3 = EmptyOperator(task_id="task_subdag", dag=subdag)
    task4 = EmptyOperator(task_id="task_subdag", dag=subdag)

    task1_2 = EmptyOperator(task_id="task1_2_subdag", dag=subdag)
    task2_2 = EmptyOperator(task_id="task1_2_subdag", dag=subdag)
    task3_2 = EmptyOperator(task_id="task1_2_subdag", dag=subdag)
    task4_2 = EmptyOperator(task_id="task1_2_subdag", dag=subdag)

    task1 >> task1_2
    task2 >> task2_2
    task3 >> task3_2
    task4 >> task4_2

    return subdag

with DAG("08-subdag-example", start_date=datetime(2024-1-4), schedule_interval="@daily") as dag:
    # DEfine tasks in the main DAG
    task1 = EmptyOperator(task_id="task1_parent_dag")
    task2 = EmptyOperator(task_id="task2_parent_dag")

    # Define a subdag
    subdag_task = SubDagOperator(
        task_id="child_dag",
        subdag=subdag(dag.dag_id, "child_dag", dag.default_args),
        dag=dag
    )