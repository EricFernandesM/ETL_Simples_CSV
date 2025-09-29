import pandas as pd
import os
import glob

#uma função que le o csv
def ler_csv(path: str) -> pd.DataFrame:
    arquivos_json = glob.glob(os.path.join(path, '*.json'))
    df_list = [pd.read_json(arquivo) for arquivo in arquivos_json]
    df_total =pd.concat(df_list, ignore_index=True)
    return 

# uma função que tranforma

# uma função que carrega o arquivo