from pathlib import Path

from extract import extrair_dados
from transform import transformar_dados
from load import carregar_dados
from logger import log


def main():
    repo_root = Path(__file__).resolve().parent.parent
    project_dir = repo_root / "engenharia-dados-do-zero"
    base_dir = project_dir if (project_dir / "data").exists() else repo_root
    caminho_arquivo = base_dir / "data" / "vendas.csv"
    caminho_banco = base_dir / "vendas.db"

    log("Iniciando pipeline")
    df = extrair_dados(caminho_arquivo)
    log("Transformando dados")
    df = transformar_dados(df)
    log("Carregando dados")
    carregar_dados(df, caminho_banco)
    log("Pipeline finalizado")

    print("Pipeline executado com sucesso")


if __name__ == "__main__":
    main()
