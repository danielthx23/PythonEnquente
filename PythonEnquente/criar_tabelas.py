from banco import oracledb, get_conexao

def rodar_arquivo_sql(file_path):
    with get_conexao() as conn:
        with conn.cursor() as cur:
            with open(file_path, 'r') as file:
                comando_sql = file.read()
                comandos = [cmd.strip() for cmd in comando_sql.split(';') if cmd.strip()]
                for comando in comandos:
                    try:
                        print(f"\nExecutando comando: {comando}\n")
                        cur.execute(comando)
                        print("Comando executado com sucesso!\n")
                    except oracledb.DatabaseError as e:
                        erro, = e.args
                        print(f"\nErro ao executar o comando: {comando}\nErro: {erro.message}")
                conn.commit() 

if __name__ == "__main__":
    rodar_arquivo_sql('./modelo.sql')