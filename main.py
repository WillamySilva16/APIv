import pandas as pd
from flask import Flask, jsonify
import pymssql
import os

app = Flask(__name__)

# ----------------------------
# 1. Conexão SQL Server
# ----------------------------
def get_sql_conn():
    server = "pbdb3073.database.windows.net"
    database = "PBDB3073"
    username = "admrs"
    password = os.getenv("Gf3$Rn8!Qb12^KsW0tZ")

    return pymssql.connect(
        server=server,
        user=username,
        password=password,
        database=database,
        port=1433
    )

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
# 3. Endpoint /data
# ----------------------------
@app.route("/data", methods=["GET"])
def data():
    df = load_data()
    return jsonify(df.to_dict(orient="records"))

@app.route("/", methods=["GET"])
def home():
    return "API ONLINE - SQL SERVER → JSON → LOOKER"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
