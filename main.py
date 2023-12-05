import mysql.connector as db

# Configurações de conexão
config = {
    'user': 'root',
    'password': '12345',
    'host': 'localhost',
    'port': 3306,
    'database': 'projeto_integrador'
}

# Conectar ao banco de dados
conn = db.connect(**config)
cursor = conn.cursor()

# Consulta SQL para selecionar todos os registros da tabela Usuarios
sql_query = "SELECT * FROM Usuarios"

# Executar a consulta
cursor.execute(sql_query)

# Recuperar os resultados da consulta em uma lista
usuarios = cursor.fetchall()

# Exibir os dados dos usuários
for usuario in usuarios:
    print("ID:", usuario[0])
    print("Login:", usuario[1])
    print("Email:", usuario[2])
    print("Tipo:", usuario[3])
    print("Status:", usuario[4])
    print("----------------------------")

    nomeUsuario = usuario[1]  # Assumindo que o login é o nome de usuário
    login = usuario[1]
    senha = "senha_padrao"  # Defina uma senha padrão ou lógica para os usuários
    email = usuario[2]
    status = usuario[4]
    tipo = usuario[3]

    SQL = "INSERT INTO usuarios(nomeUsuario, login, senha, email, status, tipo) VALUES(%s, %s, %s, %s, %s, %s)"
    PACOTE = (nomeUsuario, login, senha, email, status, tipo)

    cursor.execute(SQL, PACOTE)
    if cursor.rowcount > 0:
        print("Dados Cadastrados com Sucesso!")
    else:
        print("Erro ao Cadastrar Dados!")
    conn.commit()


# Classes para manipulação de lista duplamente encadeada
class No:
    def __init__(self, idUsuario, idDocumento, nomeDocumento):
        self.idUsuario = idUsuario
        self.idDocumento = idDocumento
        self.nomeDocumento = nomeDocumento
        self.proximo = None
        self.anterior = None


class ListaDupla:
    def __init__(self):
        self.primeiro = None
        self.ultimo = None

    def listaVazia(self):
        return self.primeiro is None

    def listaInsereFim(self, idUsuario, idDocumento, nomeDocumento):
        novoNo = No(idUsuario, idDocumento, nomeDocumento)
        if self.listaVazia():
            self.primeiro = novoNo
            self.ultimo = novoNo
        else:
            novoNo.anterior = self.ultimo
            self.ultimo.proximo = novoNo
            self.ultimo = novoNo

    def listaImprimeNos(self):
        atual = self.primeiro
        while atual:
            print("IdUsuario: ", atual.idUsuario, "; idDocumento: ", atual.idDocumento, "; nomeDocumento: ",
                  atual.nomeDocumento)
            atual = atual.proximo
        print()


# Fechar o cursor e a conexão
cursor.close()
conn.close()

