# Step 1: Import module dependencies
from typing import DefaultDict
from airflow import DAG
from datetime import datetime, time
from airflow.operators.dummy_operator import DummyOperator

# Step 2: Define default args
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2021, 6, 11),
    'retries': 0
}

# Step 3: Create a DAG object
dag = DAG(dag_id='DAG-1', default_args=default_args, catchup=False, schedule_interval='@once')

# Step 4: Create Tasks
start = DummyOperator(task_id='start', dag=dag)
end = DummyOperator(task_id='end', dag=dag)

# Step 5: Create dependencies
start >> end