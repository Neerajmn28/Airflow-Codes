from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime


# Define our task 1
def preprocess_data():
    print('Preprocessing data...')
    

# Define our task 2
def train_model():
    print('Training model...')
    
# Define our task 3
def evaluate_model():
    print('Evaluate Models')
    
# Define the DAG

with DAG(
    'ml_pipeline',
    start_date = datetime(2025,9,23),
    schedule = '@weekly'
) as dag:
    
    # Each PythonOperator wraps a function into an Airflow task, task_id → Unique name for each task. Python_callable → The actual function to run.
    
    # Define the task
    preprocess = PythonOperator(task_id = 'preprocess_task', python_callable = preprocess_data)
    train = PythonOperator(task_id = 'train_task', python_callable = train_model)
    evaluate = PythonOperator(task_id = 'evaluate_task', python_callable = evaluate_model)
    
    
    # Set dependencies
    
    preprocess >> train >> evaluate
    
    