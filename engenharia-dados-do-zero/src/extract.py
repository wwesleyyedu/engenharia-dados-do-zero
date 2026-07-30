import pandas as pd


def extrair_dados(caminho):

    try:
        df = pd.read_csv(caminho)

        print(
            f"{len(df)} registros carregados"
        )

        return df

    except Exception as erro:

        print(
            f"Erro ao carregar arquivo: {erro}"
        )

        raise