import pandas as pd
import pyodbc
from flask import Flask, jsonify
import os

app = Flask(__name__)

# ----------------------------
# 1. Conexão SQL Server
# ----------------------------
def get_sql_conn():
    server = "pbdb3073.database.windows.net"
    database = "PBDB3073"
    username = "admrs"
    password = os.getenv("DB_PASSWORD")  # senha fica no Railway

    connection_string = (
        "DRIVER={ODBC Driver 18 for SQL Server};"
        f"SERVER={server};"
        f"DATABASE={database};"
        f"UID={username};"
        f"PWD={password};"
        "Encrypt=yes;"
        "TrustServerCertificate=no;"
    )

    return pyodbc.connect(connection_string)

# ----------------------------
# 2. Consulta SQL
# ----------------------------
def load_data():
    conn = get_sql_conn()
    query = "SELECT * FROM TAB_REGISTRO_VISITA_SUPERVISAO_CABECALHO"
    df = pd.read_sql(query, conn)
    conn.close()
    return df

# ----------------------------
# 3. Endpoint para o Looker
# ----------------------------
@app.route("/data", methods=["GET"])
def data():
    df = load_data()
    return jsonify(df.to_dict(orient="records"))

@app.route("/", methods=["GET"])
def home():
    return "API ONLINE - SQL SERVER → JSON → LOOKER STUDIO"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
