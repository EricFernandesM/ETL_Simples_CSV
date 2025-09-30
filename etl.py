import pandas as pd
import os
import glob

#uma função que le o csv
def ler_csv(path: str) -> pd.DataFrame:
    arquivos_json = glob.glob(os.path.join(path, '*.json'))
    df_list = [pd.read_json(arquivo) for arquivo in arquivos_json]
    df_total =pd.concat(df_list, ignore_index=True)
    return 

# uma função que calcula o kpi de total de venda
def calcular_kpi_de_vendas_total(df: pd.DataFrame) -> pd.DataFrame:
    df["Total Venda"] = df["Quantidade"] * df["Venda"]
    return df

# uma função que carrega o arquivo

def carregar_dados(df: pd.DataFrame, format_saida: list):
    for formato in format_saida:
        if format == 'csv':
            df.to_csv("dados.csv")
        if format == 'parquet':
            df.to_parquet("dados_parquet")


