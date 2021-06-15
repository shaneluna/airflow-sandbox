# Step 1: Import module dependencies
from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago

# Step 2: Define default args
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2021, 6, 13),
    'email': ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=1)
}

# Step 3: Create a DAG object
dag = DAG(
    dag_id='spotify_dag', 
    default_args=default_args,
    description='My first DAG with ETL from spotify',
    catchup=False, 
    schedule_interval=timedelta(days=1)
)

def just_a_function():
    print("Printing from the helper function!")


# Step 4: Create Tasks
run_etl = PythonOperator(
    task_id='spotify_etl',
    python_callable=just_a_function,
    dag=dag
)

# Step 5: Create dependencies
run_etl