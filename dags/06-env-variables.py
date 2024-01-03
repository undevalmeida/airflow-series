from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.models import Variable
from airflow.hooks.base import BaseHook
import datetime

def get_env():
    env_var_test = Variable.get("ENV_VAR_TEST")
    env_json_var_test = Variable.get("ENV_JSON_VAR_TEST")

    print(f"ENV_VAR_TEST: {env_var_test}")
    print(f"ENV_JSON_VAR_TEST: {env_json_var_test}")


def get_conn(): # é mais seguro utilizar conection quando existe uma conexão entre banco de dados, servidores, etc.
    airflow_conn = BaseHook.get_connection("MY_PROD_DATABASE")
    airflow_conn_pass = airflow_conn.password

    print(f"MY_PROD_DATABASE: {airflow_conn}")
    print(f"MY_PROD_DATABASE: {airflow_conn_pass}")

with DAG(
    dag_id='06-env-variables',
    start_date=datetime.datetime(2024,1,1),
    schedule=None
) as dag:
    test_task = PythonOperator(task_id = 'test_task', python_callable=get_env)

    test_task2 = PythonOperator(task_id = 'test_task2', python_callable=get_conn)