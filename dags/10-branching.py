from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import BranchPythonOperator
from datetime import datetime, timedelta

default_args = {
    "owner":"airflow",
    "start_date": datetime(2024,1,6),
    "depends_on_past": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=5)
}

dag = DAG(
    "10-branching-example",
    default_args=default_args,
    catchup=False,
    schedule_interval="@daily"
)

def should_run(**context):
    """ 
    A Python callable that returns the task ID or list of task IDs to run next based on some condition.
    """

    # Deternube the date
    today = datetime.now().strftime("%A")

    # Define the tasks to run for each day of the week
    if today == "Monday":
        return "print_whoami"
    elif today == "Tuesday":
        return "print_date"
    elif today == "Wednesday":
        return ["print_whoami", "print_date"]
    else:
        return "print_nothing"

# Define the tasks    
print_whoami = BashOperator(
    task_id = "print_whoami",
    bash_command="whoami",
    dag=dag
)

print_date = BashOperator(
    task_id = "print_date",
    bash_command="date",
    dag=dag
)

print_nothing = BashOperator(
    task_id="print_nothing",
    bash_command="echo 'Nothing to print today'",
    dag=dag
)
branching_task = BranchPythonOperator(
    task_id = "branching_task",
    python_callable=should_run,
    provide_context=True,
    dag=dag
)

# Define the task dependencies

branching_task >> [print_whoami, print_date, print_nothing]
