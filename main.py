import os
import pyodbc
import pandas as pd
from fastapi import FastAPI
from dotenv import load_dotenv

load_dotenv()
app = FastAPI()

def get_connection():
    server = os.getenv("DB_HOST")
    database = os.getenv("DB_NAME")
    username = os.getenv("DB_USER")
    password = os.getenv("DB_PASS")

    conn_str = (
        "DRIVER={ODBC Driver 17 for SQL Server};"
        f"SERVER={server};"
        f"DATABASE={database};"
        f"UID={username};"
        f"PWD={password}"
    )
    return pyodbc.connect(conn_str)

@app.get("/")
def root():
    return {"status": "API ONLINE"}

@app.get("/visitas")
def visitas():
    conn = get_connection()
    df = pd.read_sql_query("SELECT TOP 100 * FROM TAB_REGISTRO_VISITA_SUPERVISAO_CABECALHO", conn)
    conn.close()
    return df.to_dict(orient="records")
