from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2023, 5, 19)
}


dag = DAG('Dag_Tareas', default_args=default_args, schedule_interval=None)


task1 = BashOperator(
    task_id='Ejecutar_Extraer',
    bash_command='python Extraer.py',
    dag=dag
)

task2 = BashOperator(
    task_id='Ejecutar_Transformar',
    bash_command='python Transformar.py',
    dag=dag
)

task3 = BashOperator(
    task_id='Ejecutar_cargar',
    bash_command='python Cargar.py',
    dag=dag
)


