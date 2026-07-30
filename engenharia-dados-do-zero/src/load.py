import sqlite3
from pathlib import Path


def carregar_dados(df, caminho_banco):
    caminho_banco = Path(caminho_banco)
    conn = sqlite3.connect(str(caminho_banco))

    df.to_sql(
        "vendas",
        conn,
        if_exists="replace",
        index=False
    )

    conn.close()