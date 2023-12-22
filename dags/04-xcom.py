from airflow import DAG
from airflow.operators.python import PythonOperator

from datetime import datetime

def ingest():
    import pandas as pd
    url = 'https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos/vendas-gasolina-c-m3-2020.csv'

    df = pd.read_csv(url, delimiter=';', encoding='utf-8')

with DAG(
    dag_id='04-xcoms'
    , start_date=datetime(2023, 12, 21)) as dag:

    task1 = PythonOperator(task_id='ingest', python_callable=)

    task2 = PythonOperator(task_id='consume', python_callable=)