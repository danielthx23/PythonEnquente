import oracledb
from oracledb import Connection as conn
import os

def get_conexao() -> conn:
    #usuario = os.getenv("USER_ORA")
    #senha = os.getenv("PWD_ORA")
    return oracledb.connect(user='rm558263', password='071005', dsn='oracle.fiap.com.br/orcl')

def insere_enquente(enq: dict):
    sql = "insert into tbr_enquente(nome, categoria) values(:nome, :categoria) returning id into :id"
    dado = {"nome": enq['nome'], "categoria": enq['categoria']}
    with get_conexao() as conn:
        with conn.cursor() as curr:
            novo_id = curr.var(oracledb.NUMBER)
            dado['id'] = novo_id
            curr.execute(sql, dado)
            enq['id'] = novo_id.getvalue()[0]
        conn.commit()

def insere_pergunta(perg: dict):
    sql = "insert into tbr_pergunta(texto, tipo, numero, id_enquente) values(:texto, :tipo, :numero, :id_enquente) returning id into :id"
    with get_conexao() as conn:
        with conn.cursor() as curr:
            novo_id = curr.var(oracledb.NUMBER)
            perg['id'] = novo_id
            curr.execute(sql, perg)
            perg['id'] = novo_id.getvalue()[0]
        conn.commit()

def insere_opcao(opcao: dict):
    sql = "insert into tbr_opcoes(alternativa, rotulo, id_pergunta) values(:alternativa, :rotulo, :id_pergunta)"
    with get_conexao() as conn:
        with conn.cursor() as curr:
            curr.execute(sql, opcao)
        conn.commit()