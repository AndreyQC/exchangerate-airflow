from datetime import datetime
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator

with DAG(dag_id="0_first_dummy_dag_consume_data_from_pos",
        start_date=datetime(2022,4,25),
        schedule_interval=None) as dag:
    
    get_new_data = DummyOperator(task_id="get_new_data")
    parse_file = DummyOperator(task_id="parse_file")
    check_if_new_customer = DummyOperator(task_id="check_if_new_customer")
    create_new_customer = DummyOperator(task_id="create_new_customer")
    update_existing_customer = DummyOperator(task_id="update_existing_customer")

    get_new_data >> parse_file >> check_if_new_customer >> [create_new_customer, update_existing_customer]