from fastapi import FastAPI
import pymssql
import os

app = FastAPI()

# Função de conexão ao SQL Server
def connect_db():
    return pymssql.connect(
        server=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASS"),
        database=os.getenv("DB_NAME")
    )

@app.get("/")
def home():
    return {"status": "API ONLINE — SQL SERVER → JSON"}

@app.get("/data")
def get_data():
    conn = connect_db()
    cursor = conn.cursor(as_dict=True)

    # 🔥 AJUSTE AQUI: NOME DA SUA TABELA
    query = "SELECT TOP 50 * FROM TAB_REGISTRO_VISITA_SUPERVISAO_CABECALHO"  
    cursor.execute(query)

    rows = cursor.fetchall()

    cursor.close()
    conn.close()

    return rows
