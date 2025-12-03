import os
import pandas as pd
from fastapi import FastAPI
import pytds

app = FastAPI()

DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")

def run_query(query):
    with pytds.connect(
        server=DB_HOST,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASS,
        port=1433,
        as_dict=True
    ) as conn:
        with conn.cursor() as cursor:
            cursor.execute(query)
            return cursor.fetchall()

@app.get("/")
def home():
    return {"status": "ok"}

@app.get("/visitas")
def visitas():
    sql = "SELECT TOP 10 * FROM TAB_REGISTRO_VISITA_SUPERVISAO_CABECALHO"
    data = run_query(sql)
    return data
