import csv
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
from pathlib import Path

def leer_archivo_csv(archivo_csv):
    with open(archivo_csv, 'r') as file:
        reader = csv.reader(file)
        data = list(reader)
    return data

def read_csv_file():
    return leer_archivo_csv('map.csv')


dag = DAG(
    'Extraer_data_dag',
    description='Tarea PythonOperator de Airflow leer archivo map.CSV',
    schedule_interval=None, 
    start_date=datetime(2023, 5, 19),  
    catchup=False  
)

read_csv_task = PythonOperator(
    task_id='read_csv_file_task',
    python_callable=read_csv_file,
    dag=dag
)

read_csv_task