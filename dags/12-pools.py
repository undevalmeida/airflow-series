from airflow.decorators import dag
from airflow.operators.empty import EmptyOperator
from datetime import datetime

@dag(
    dag_id="12-polls_exmple",
    start_date=datetime(2024,1,8),
    schedule=None
)
def example_pools():
    # Monthly
    t1 = EmptyOperator(task_id="t1", pool="pool_example", priority_weight=1)
    t2 = EmptyOperator(task_id="t2", pool="pool_example", priority_weight=1)
    t3 = EmptyOperator(task_id="t3", pool="pool_example", priority_weight=1)
    # Weekly
    t4 = EmptyOperator(task_id="t4", pool="pool_example", priority_weight=5)
    t5 = EmptyOperator(task_id="t5", pool="pool_example", priority_weight=5)
    t6 = EmptyOperator(task_id="t6", pool="pool_example", priority_weight=5)
    # Daily
    t7 = EmptyOperator(task_id="t7", pool="pool_example", priority_weight=10)
    t8 = EmptyOperator(task_id="t8", pool="pool_example", priority_weight=10)
    t9 = EmptyOperator(task_id="t9", pool="pool_example", priority_weight=10)

    t1 >> [t2, t3]

    t4 >> [t5, t6]

    t7 >> [t8, t9]

examples_pools = example_pools()