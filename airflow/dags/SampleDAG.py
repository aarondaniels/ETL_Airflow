from datetime import datetime
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago

#These args will get passed on to the python operator
default_args = {
    'owner': 'XXX',
    'depends_on_past': False,
    'start_date': days_ago(2),
    'email': ['XXXX@YYY.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
}

#Define python function
def square(x):
    return x**2

#Define DAG object
dag = DAG(
    'python_square_operator',
    description = 'Squaring a number using Airflow',
    schedule_interval = '0 12 * * *',
    Start_date = datetime(2017,3,20), catchup = False)

#Define task
t1 = PythonOperator(
    task_id = 'square',
    python_callable= square, 
    op_kwargs = {"x": 13},
    dag=dag
)

t1


