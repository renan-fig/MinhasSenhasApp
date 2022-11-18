import mysql.connector 

def cria_conexao():
    conexao = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = '',       
        database = 'appsenha'
    )
    return conexao

conexao = cria_conexao()

def cria_cursor():
    cursor = conexao.cursor()
    return cursor

cursor = cria_cursor()

def executa_query(query):
    print(query)
    cursor.execute(query)
    conexao.commit()
    print("Query executada com sucesso!")

#cursor.execute('create database appsenha')
#cursor.execute("create table usuario( cod_user int(10) PRIMARY KEY AUTO_INCREMENT, plataforma char(30), email varchar(50), senha varchar(30))")

    