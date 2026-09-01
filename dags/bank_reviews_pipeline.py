from datetime import datetime

from airflow import DAG
from airflow.operators.empty import EmptyOperator
from airflow.operators.bash import BashOperator
from airflow.providers.docker.operators.docker import DockerOperator
from docker.types import Mount


with DAG(
    dag_id="bank_reviews_pipeline",
    start_date=datetime(2026, 7, 12),
    schedule="@daily",
    catchup=False,
    tags=["bank", "elt"],
) as dag:

    start = EmptyOperator(task_id="start")

    scraping = DockerOperator(
        task_id="scraping",
        image="bank-scraper:latest",
        command="python -m src.scraping.pipeline",
        docker_url="unix://var/run/docker.sock",
        network_mode="modern-bank-reviews-data-warehouse_default",
        auto_remove="success",
        mounts=[
            Mount(
                source=r"C:\Users\Soumia\Desktop\modern-bank-reviews-data-warehouse",
                target="/workspace",
                type="bind",
            )
        ],
        working_dir="/workspace",
        mount_tmp_dir=False,
    )

    nlp = BashOperator(
        task_id="nlp",
        bash_command="cd /opt/airflow && python -m src.nlp.pipeline",
    )

    dbt_run = BashOperator(
        task_id="dbt_run",
        bash_command="cd /opt/airflow/bank_reviews_dbt && dbt run --profiles-dir /home/airflow/.dbt",
    )

    dbt_test = BashOperator(
        task_id="dbt_test",
        bash_command="cd /opt/airflow/bank_reviews_dbt && dbt test --profiles-dir /home/airflow/.dbt",
    )

    end = EmptyOperator(task_id="end")

    start >> scraping >> nlp >> dbt_run >> dbt_test >> end