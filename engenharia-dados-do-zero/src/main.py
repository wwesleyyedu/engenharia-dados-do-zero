from pathlib import Path
from datetime import datetime

def log(mensagem):
    agora = datetime.now()
    print(f"[{agora}] {mensagem}")

from extract import extrair_dados
from transform import transformar_dados
from load import carregar_dados

def main():
    base_dir = Path(__file__).resolve().parent.parent
    caminho_arquivo = base_dir / "data" / "vendas.csv"
    caminho_banco = base_dir / "vendas.db"

    df = extrair_dados(caminho_arquivo)
    df = transformar_dados(df)
    carregar_dados(df, caminho_banco)

    print("Pipeline executado com sucesso")


if __name__ == "__main__":
    main()

    log("Iniciando pipeline")

df = extrair_dados(
    "data/vendas.csv"
)

log("Transformando dados")

df = transformar_dados(df)

log("Carregando dados")

carregar_dados(df)

log("Pipeline finalizado")