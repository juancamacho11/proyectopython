import csv
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
from pathlib import Path

def export_transformed_data():
    input_file_path = r"TransformarMap.csv"
    output_file_path = r"CargaMap.csv"
    
    with open(input_file_path, 'r') as input_file, open(output_file_path, 'w', newline='') as output_file:
        csv_reader = csv.reader(input_file)
        csv_writer = csv.writer(output_file)
        
        for row in csv_reader:

            csv_writer.writerow(row)

dag = DAG(
    'Cargar_data_dag',
    description='Tarea de Airflow PythonOperator para cargar datos transformados',
    schedule_interval=None,  # Para ejecutar manualmente o según sea necesario
    start_date=datetime(2023, 5, 19),  # Fecha de inicio de la tarea
    catchup=False 
)


export_data_task = PythonOperator(
    task_id='export_transformed_data_task',
    python_callable=export_transformed_data,
    dag=dag
)


export_data_task