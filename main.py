from fastapi import FastAPI
import pymssql
import os

app = FastAPI()

DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")

def conectar():
    return pymssql.connect(
        server=DB_HOST,
        user=DB_USER,
        password=DB_PASS,
        database=DB_NAME
    )

@app.get("/")
def home():
    return {"status": "API funcionando"}

@app.get("/visitas")
def visitas():
    conn = conectar()
    cursor = conn.cursor(as_dict=True)
    cursor.execute("SELECT TOP 100 * FROM TAB_REGISTRO_VISITA_SUPERVISAO_CABECALHO")
    dados = cursor.fetchall()
    conn.close()
    return dados
