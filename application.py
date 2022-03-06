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
        #print(cursor.execute("SELECT * FROM information_schema.tables',"))

    # inserir valores
    def insertSQL2(id):
        print("Atributos de " + v[id][0] + " sao: " + v[id][1])
        qi = ['INSERT INTO  ', ''.join(v[id]),' VALUES (']
        qi = ''.join(qi)
        for x in range(t[id]):
            h = input("Insira o valor do " + str(x+1) + " Argumento: ")
            if(x==0):
                qi = [qi, h]
            else:
                qi = [qi, ',', h]
            qi = ''.join(qi)
        qf = [qi, ')']
        q2 = ''.join(qf)
        print(q2)
        sql = q2
        cursor.execute(sql)
        connection.commit()
        

    # atualizar valor
    def updateSQL(id):
        print("Atributos de " + v[id][0] + " sao: " + v[id][1])
        atributo = input("Digite o atributo a ser alterado: ")
        valor = input("Digite o valor a ser atribuido: ")
        codigo_f = input("Digite a variavel primaria: ")
        codigo = input("Digite o codigo mumerico: ")
        q1 = ['UPDATE ', v[id][0],' SET ',atributo,' = ', valor, ' WHERE ', codigo_f ,'= ', codigo]
        sql = ''.join(q1) 
        cursor.execute(sql)
        connection.commit()

        
    # deletar valores
    def deleteSQL(id): 
        print("Atributos de " + v[id][0] + " sao: " + v[id][1])
        codigo_f = input("Digite a chave primaria a ser excluida(primeira): ")
        codigo = input("Digite o codigo mumerico: ")
        q1 = ['DELETE ', ' FROM ', v[id][0] , ' WHERE ', codigo_f ,'= ', codigo]
        sql = ''.join(q1) 
        cursor.execute(sql)
        connection.commit()

    def viewtable(id):
        #print(v[id][0])
        q1 = [z,v[id][0]]
        q2 = ''.join(q1)
        sql = q2
        cursor.execute(sql)
        rows = cursor.fetchall()
        for row in rows:
            print(row)



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
        interface = " \nDigite um número\n\n 1. Criar tabela\n 2. Inserir valores\n 3. Atualizar tabela\n 4. Deletar valores\n 5. Comando select\n 6. Mostrar tabelas\n 0. Sair\n"
        print(interface)

        # numero da query a ser executada
        query = int(input())
        if query < 0 or query > 10:
            print("Erro tente novamente")
            query = int(input())

        if query == 0:
               
            break

        if query == 1:
            createSQL()

        if query == 2:
            for x in range(15):
                print("ID: " + str(x) +"  " + v[x][0])
            pe = input("Digite o numero da tabela a qual deseja inserir: ")
            pe = int(pe)
            insertSQL2(pe)
            #insertSQL()
            print("inserido")

        if query == 3:
            for x in range(15):
                print("ID: " + str(x) +"  " + v[x][0])
            pe = input("Digite o numero da tabela a ser atualizada: ")
            pe = int(pe)
            updateSQL(pe)
            print("Atualizado")

        if query == 4:
            for x in range(15):
                print("ID: " + str(x) +"  " + v[x][0])
            pe = input("Digite o numero da tabela a ter uma linha excluida: ")
            pe = int(pe)
            deleteSQL(pe)
            print("Excluido com sucesso")
            
        if query == 5:
            selectSQL()

        if query == 6:
            for x in range(15):
                print("ID: " + str(x) +"  " + v[x][0])
            pe = input("Digite o numero da tabela a ser consultada: ")
            pe = int(pe)
            viewtable(pe)

except (Exception, Error) as error:
    print("Erro de conexão com o PostgreSQL", error)
finally:
    if (connection):
        cursor.close()  
        connection.close()
        print("Conexão terminada")