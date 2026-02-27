from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import requests
import psycopg2
import csv
import io

def load_covid_data():

    url = "https://covid.ourworldindata.org/data/owid-covid-data.csv"
    
    response = requests.get(url)
    response.raise_for_status()

    conn = psycopg2.connect(
        host="postgres",
        database="covid",
        user="airflow",
        password="airflow"
    )
    cur = conn.cursor()

    cur.execute("""
        CREATE SCHEMA IF NOT EXISTS raw;
        CREATE TABLE IF NOT EXISTS raw.covid_data (
            location TEXT,
            date DATE,
            total_cases FLOAT,
            new_cases FLOAT,
            total_deaths FLOAT,
            new_deaths FLOAT
        );
    """)

    csv_data = csv.DictReader(io.StringIO(response.text))

    for row in csv_data:
        cur.execute("""
            INSERT INTO raw.covid_data
            VALUES (%s,%s,%s,%s,%s,%s)
        """, (
            row["location"],
            row["date"],
            row["total_cases"],
            row["new_cases"],
            row["total_deaths"],
            row["new_deaths"],
        ))

    conn.commit()
    cur.close()
    conn.close()

with DAG(
    dag_id="covid_etl",
    start_date=datetime(2024,1,1),
    schedule_interval="@daily",
    catchup=False
) as dag:

    load_task = PythonOperator(
        task_id="load_covid_data",
        python_callable=load_covid_data
    )

    load_task
