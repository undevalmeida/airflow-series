from airflow import DAG
from airflow.operators.python import PythonOperator

from datetime import datetime

def ingest(**kwargs):
    import pandas as pd
    url = 'https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos/vendas-gasolina-c-m3-2020.csv'

    df = pd.read_csv(url, delimiter=';', encoding='utf-8')

    df.columns = [column.strip() for column in df.columns]

    id_vars = ['COMBUSTÍVEL', 'ANO', 'REGIÃO', 'ESTADO', 'UNIDADE', 'TOTAL']
    
    value_vars = [column for column in df.columns if column not in id_vars]

    column_to_be_cleaned = value_vars + ['TOTAL']

    df_cleaned = df.copy()
    df_cleaned = df.fillna(0)

    for column in column_to_be_cleaned:
        df_cleaned[column] = df_cleaned[column].apply(lambda x: str(x).replace('.', '')).astype(int)

    df_melted = pd.melt(df_cleaned, id_vars=id_vars, value_vars=value_vars)
    df_melted['contribution'] = df_melted['value']/df_melted['TOTAL']
    df_melted['contribution_%'] = df_melted['value']/df_melted['TOTAL'] * 100

    max_contribution = df_melted['contribution'].max()
    min_contribution = df_melted[df_melted['contribution']!= 0]['contribution'].min()

    #max_contribution_row = df_melted[df_melted['contribution']==max_contribution]
    #min_contribution_row = df_melted[df_melted['contribution']==min_contribution]
    """ 
    ti = kwargs['ti']
    ti.xcom_push(key='max_contribution', value=max_contribution)
    ti.xcom_push(key='min_contribution', value=min_contribution) """
    return{'max_contribution':max_contribution, 'min_contribution':min_contribution}

def consume(xcom):
    from json import loads

    return_value = loads(xcom.replace("'", '"')) # Fazendo replace porque o json contém apenas aspas duplas
    """ 
    max_contribution = ti.xcom_pull(key='max_contribution', task_ids='ingest')
    min_contribution = ti.xcom_pull(key='min_contribution', task_ids='ingest') """
    
    max_contribution = return_value['max_contribution']
    min_contribution = return_value['min_contribution']
   
    print(return_value)
    print(f"tipo de dado: {type(return_value)}")
    
    print(f'max_contribution {max_contribution}')
    print(f'min_contribution {min_contribution}')
with DAG(
    dag_id='04-xcoms'
    , start_date=datetime(2023, 12, 21)
    , schedule=None
    ) as dag:

    task1 = PythonOperator(task_id='ingest', python_callable=ingest)

    task2 = PythonOperator(
        task_id='consume'
        , python_callable=consume
        , op_kwargs={
            'xcom' : "{{ti.xcom_pull(key='return_value', task_ids='ingest')}}"
        }
        )

    task1 >> task2