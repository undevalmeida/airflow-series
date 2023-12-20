from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def function_example(position:str):
    """
    Função responsável por printar na tela um texto teste

    Args:
        posicao(str): determina a posicao desejada para ser colocada na string
    """

    print(f"Testando minha {position} função python")


with DAG(
    dag_id='02-python_operator_example'
    , start_date=datetime(2023,12,19), schedule=None) as dag:

    task1 = PythonOperator(
        task_id = 'first_function',
        python_callable = function_example,
        op_args = ['first']
    )

    task2 = PythonOperator(
        task_id = 'second_function',
        python_callable = function_example,
        op_kwargs = { # recebe dicionário
            'position' : 'second'
        }
    )