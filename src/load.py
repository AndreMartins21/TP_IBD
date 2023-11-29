import mariadb
from db_connect import MariaDB
from typing import List, Tuple
import pandas as pd


class Loader:
    def __init__(self):
        self.conn = MariaDB().get_connect()
    
    def load(self, table_name: str, df: pd.DataFrame):
        rows_values = self.get_rows_values(df)

        try:
            with self.conn.cursor() as cursor:
                for row_value in rows_values:
                    try:                  
                        cursor.execute(
                            f""" 
                            INSERT INTO {table_name}
                            VALUES
                            {row_value}
                            ;                        
                            """
                        )
                    except Exception as e:
                        print(f"Erro ao inserir tupla: {e}")
                        continue
            print(f"[+] Arquivos carregados com sucesso na tabela {table_name}!")
            self.conn.commit()
            self.conn.close()

        except mariadb.Error as e:
            self.conn.close()
            print()
            print(f"Erro ao inserir na tabela {table_name}: {e}")
            print()
            raise e

    @staticmethod
    def get_rows_values(df: pd.DataFrame) -> str:
        try:
            for _, row in df.iterrows():
                row = row.replace([pd.NaT, 'NaT', 'nan'], None)
                row_value = str(tuple(row.values))
                yield row_value
        except Exception as e:
            print(f"Erro ao converter df to list of tuples: {e}")

if __name__ == "__main__":
    # Testando conexão com o BD e carregamento de informações
    maria_db = MariaDB()
    conn = maria_db.connect()

    with conn.cursor() as cursor:
        try:
            cursor.execute(
                "INSERT INTO teste (random_number) VALUES (1), (2), (3), (4);"
            )
            print("Inseriu!")
        except mariadb.Error as e: 
            print(f"Erro: {e}")

    conn.commit() 
