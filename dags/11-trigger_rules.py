from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.decorators import task_group
from datetime import datetime, timedelta

default_args = {
    "owner":"airflow",
    "start_date": datetime(2024,1,6),
    "depends_on_past": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=5)
}

dag = DAG(
    "11-trigger-rules",
    default_args=default_args,
    schedule_interval="@daily"
)

t1 = BashOperator(
    task_id = "t1",
    bash_command="echo 'Hello from task 1'",
    dag=dag
)

@task_group(group_id="first_tg", dag=dag)
def dummy_task_group():
    t2 = BashOperator(
        task_id="t2",
        bash_command="echo 'Hello from task 2'",
        dag=dag,
        trigger_rule="none_failed"
    )

    t3 = BashOperator(
        task_id="t3",
        bash_command="echo 'Hello from task 3'",
        dag=dag,
        trigger_rule="one_failed"
    )

    t4 = BashOperator(
        task_id="t4",
        bash_command="echo 'Hello from task 4'",
        dag=dag,
        trigger_rule="one_success"
    )

    [t2,t3,t4]

@task_group(group_id="second_tag",dag=dag)
def dummy_task_group2():
    t5 = BashOperator(
        task_id="t5",
        bash_command="echo 'Hello from task 5'",
        dag=dag,
        trigger_rule="none_failed"
    )

    t6 = BashOperator(
        task_id="t6",
        bash_command="echo 'Hello from task 6'",
        dag=dag,
        trigger_rule="none_skipped"
    )

    t7 = BashOperator(
        task_id="t7",
        bash_command="echo 'Hello from task 7'",
        dag=dag,
        trigger_rule="all_done"
    )

    [t5,t6,t7]

t8 = BashOperator(
    task_id="t8",
    bash_command="echo 'Hello from task 8'",
    dag=dag,
    trigger_rule="dummy"
)

t1 >> dummy_task_group() >> dummy_task_group2() >> t8