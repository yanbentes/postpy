# aplicação para banco de dados postgresql
import psycopg2
from psycopg2 import Error

try:
    # conexão com o banco de dados
    connection = psycopg2.connect(user="user",
                                  password="password",
                                  host="host",
                                  port="port",
                                  database="db")

    # cursor 
    cursor = connection.cursor()
    # versão do PostgreSQL
    cursor.execute("SELECT version();")
    record = cursor.fetchone()
    print(record)

    # definições das funções

    # criar tabela
    def createSQL():
        create_table_query = "CREATE TABLE " +  input("CREATE TABLE ")
        cursor.execute(create_table_query)
        connection.commit()
        # print(cursor.execute("SELECT * FROM information_schema.tables;"))

    # inserir valores
    def insertSQL():
        insert_query = "INSERT INTO " + input("INSERT INTO ")
        cursor.execute(insert_query)
        connection.commit()

    # atualizar valor
    def updateSQL():
        update_query = "UPDATE " + input("UPDATE ")
        cursor.execute(update_query)
        connection.commit()

    # deletar valores
    def deleteSQL(): 
        delete_query = "DELETE FROM " + input("DELETE FROM ")
        cursor.execute(delete_query)
        connection.commit()

    # query personalizada
    def selectSQL():
        select_query = "SELECT " + input("SELECT ")
        cursor.execute(select_query)
        myresult = cursor.fetchall()

        for x in myresult:
          print(x)
        #connection.commit()

    # interface    
    teste = 1

    while  teste == 1:
        interface = " \nDigite um número\n\n 1. Criar tabela\n 2. Inserir valores\n 3. Atualizar tabela\n 4. Deletar valores\n 5. Comando select\n 6. Listar tabelas\n 0. Sair\n"
        print(interface)

        # numero da query a ser executada
        query = int(input())
        if query < 0 or query > 6:
            print("Erro tente novamente")
            query = int(input())

        if query == 0:
            break

        if query == 1:
            createSQL()

        if query == 2:
            insertSQL()

        if query == 3:
            updateSQL()

        if query == 4:
            deleteSQL()

        if query == 5:
            selectSQL()

        if query == 6:
            cursor.execute("SELECT table_name FROM information_schema.tables WHERE table_schema = 'public'")
            for table in cursor.fetchall():
                print(table)
            

except (Exception, Error) as error:
    print("Erro de conexão com o PostgreSQL", error)
finally:
    if (connection):
        cursor.close()  
        connection.close()
        print("Conexão terminada")
