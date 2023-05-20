import csv
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
from pathlib import Path

def clean_and_transform_data():
    file_path = r"map.csv"
    output_path = r"TransformarMap.csv"
    
    cleaned_data = []
    
    with open(file_path, 'r') as input_file:
        csv_reader = csv.reader(input_file)

        header = next(csv_reader)
        cleaned_data.append(header)
        
        for row in csv_reader:
            if any(value == '' for value in row):
                continue  

            if row in cleaned_data:
                continue  
            transformed_row = [value if value != 'null' else '0' for value in row]
            
            cleaned_data.append(transformed_row)
    
    with open(output_path, 'w', newline='') as output_file:
        csv_writer = csv.writer(output_file)
        csv_writer.writerows(cleaned_data)


dag = DAG(
    'Transformar_data_dag',
    description='Tarea de PythonOperator Airflow para limpiar y transformar datos',
    schedule_interval=None,  
    start_date=datetime(2023, 5, 23),  
    catchup=False  
)

clean_data_task = PythonOperator(
    task_id='clean_and_transform_data_task',
    python_callable=clean_and_transform_data,
    dag=dag
)

clean_data_task