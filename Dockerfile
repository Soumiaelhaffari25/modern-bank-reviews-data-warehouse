FROM apache/airflow:3.3.0

COPY requirements-airflow.txt /requirements-airflow.txt

USER airflow

RUN pip install --upgrade pip

RUN pip install --no-cache-dir -r /requirements-airflow.txt

RUN python -m playwright install chromium