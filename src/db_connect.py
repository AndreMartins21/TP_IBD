import mariadb
import sys
import os


class MariaDB:
    def __init__(self):
        pass

    def get_connect(self) -> mariadb.Connection:
        print("Criando conexão com o MariaDB")
        try:
            conn = mariadb.connect(
                user=os.getenv("user"),
                password=os.getenv("password"),
                host=os.getenv("host"),
                port=int(os.getenv("port")),
                database=os.getenv("database")
            )

            return conn
        except mariadb.Error as e:
            print(f"Error connecting to MariaDB Platform: {e}")
            sys.exit(1)

    def create_tables(self, file_sql: str):
        print("[+] Criando tabelas para inserir os dados!")
        
        with open(file_sql, mode="r", encoding="utf8") as f:
            str_file_sql = f.read()
        
        list_queries = str_file_sql.split(";")

        conn = self.get_connect()
        
        with conn.cursor() as cursor:
            for i, query in enumerate(list_queries[:-1]):
                print(f"Rodando {i+1}° query de {len(list_queries)}")

                query = query + ";"

                try:
                    cursor.execute(query)
                except Exception as e:
                    print(f"Erro ao rodar {i+1}° query: {e}")
        conn.commit()
        conn.close()
                


if __name__ == "__main__":
    # Get Cursor
    maria_db = MariaDB()
    conn = maria_db.connect()

    cur = conn.cursor()
