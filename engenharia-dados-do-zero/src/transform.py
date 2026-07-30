def transformar_dados(df):

    df["valor_total"] = (
        df["quantidade"]
        * df["preco_unitario"]
    )

    return df