import pandas as pd
import os
from db_connect import MariaDB
from transformation import Transform
from load import Loader


class Main(Transform):
    def __init__(self):
        self.df_demo_contabil = pd.DataFrame()
        self.df_oper_benef = pd.DataFrame()
        self.df_relatorio = pd.DataFrame()

    def read_datasets(self, path_datasets: str):
        os.chdir(path_datasets)
        
        self.df_demo_contabil = pd.read_csv("2t2023.csv", sep = ";")
        self.df_oper_benef = pd.read_csv("Beneficiarios_operadora_e_carteira.csv", sep = ";")
        self.df_relatorio = pd.read_csv("Relatorio_cadop.csv", sep = ";")

        os.chdir("../../../src")
    
    def transform(self):
        try:
            # Renomeando colunas para o nome das colunas nas tabelas
            super().rename_columns()
        

            # Lidando com valores NaN
            super().resolve_null_values()
        
            # Padronizando valores:
            super().standardize_double()
            super().standardize_int()
            super().standardize_str()
        except Exception as e:
            print(f"Erro ao transformar data.frames: {e}")
            raise e
        
    def load_data(self):
        Loader().load(
            table_name = "relatorio",
            df = self.df_relatorio
        )

        Loader().load(
            table_name = "operadora_beneficiario",
            df = self.df_oper_benef
        )

        Loader().load(
            table_name = "demo_contabil",
            df = self.df_demo_contabil
        )
        pass

if __name__ == "__main__":
    main = Main()

    MariaDB().create_tables(file_sql = "src/code_create_table.sql")

    main.read_datasets(
        path_datasets="data/datasets/datasets_union"
    )

    main.transform()
    main.load_data()
    a = 2