import pickle

class Livro:
    def __init__(self, titulo, autor, ano):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.disponivel = True

class Usuario:
    def __init__(self, nome, username, senha):
        self.nome = nome
        self.username = username
        self.senha = senha
        self.livros_emprestados = []

class Biblioteca:
    def __init__(self):
        self.livros = []
        self.usuarios = []
        self.usuario_atual = None
        self.carregar_dados()

    def salvar_dados(self):
        with open('biblioteca.pkl', 'wb') as f:
            pickle.dump((self.livros, self.usuarios), f)

    def carregar_dados(self):
        try:
            with open('biblioteca.pkl', 'rb') as f:
                self.livros, self.usuarios = pickle.load(f)
        except FileNotFoundError:
            self.livros = []
            self.usuarios = []

    def adicionar_livro(self, titulo, autor, ano):
        novo_livro = Livro(titulo, autor, ano)
        self.livros.append(novo_livro)
        self.salvar_dados()
        print(f'Livro "{titulo}" adicionado com sucesso.')

    def buscar_livro(self, titulo=None, autor=None):
        resultados = []
        for livro in self.livros:
            if (titulo and titulo.lower() in livro.titulo.lower()) or (autor and autor.lower() in livro.autor.lower()):
                resultados.append(livro)
        return resultados

    def listar_livros(self):
        if not self.livros:
            print("Nenhum livro na biblioteca.")
        for livro in self.livros:
            status = "Disponível" if livro.disponivel else "Emprestado"
            print(f'Título: {livro.titulo}, Autor: {livro.autor}, Ano: {livro.ano}, Status: {status}')

    def emprestar_livro(self, titulo):
        if self.usuario_atual:
            for livro in self.livros:
                if livro.titulo.lower() == titulo.lower() and livro.disponivel:
                    livro.disponivel = False
                    self.usuario_atual.livros_emprestados.append(livro)
                    self.salvar_dados()
                    print(f'Livro "{titulo}" emprestado com sucesso.')
                    return
            print(f'Livro "{titulo}" não está disponível para empréstimo.')
        else:
            print("Você precisa estar logado para emprestar um livro.")

    def devolver_livro(self, titulo):
        if self.usuario_atual:
            for livro in self.usuario_atual.livros_emprestados:
                if livro.titulo.lower() == titulo.lower():
                    livro.disponivel = True
                    self.usuario_atual.livros_emprestados.remove(livro)
                    self.salvar_dados()
                    print(f'Livro "{titulo}" devolvido com sucesso.')
                    return
            print(f'Você não possui o livro "{titulo}" para devolver.')
        else:
            print("Você precisa estar logado para devolver um livro.")

    def registrar_usuario(self, nome, username, senha):
        for usuario in self.usuarios:
            if usuario.username == username:
                print("Username já existe. Tente novamente.")
                return
        novo_usuario = Usuario(nome, username, senha)
        self.usuarios.append(novo_usuario)
        self.salvar_dados()
        print(f'Usuário "{nome}" registrado com sucesso.')

    def login_usuario(self, username, senha):
        for usuario in self.usuarios:
            if usuario.username == username and usuario.senha == senha:
                self.usuario_atual = usuario
                print(f'Usuário "{username}" logado com sucesso.')
                return
        print("Username ou senha incorretos. Tente novamente.")

    def logout_usuario(self):
        if self.usuario_atual:
            print(f'Usuário "{self.usuario_atual.username}" deslogado com sucesso.')
            self.usuario_atual = None
        else:
            print("Nenhum usuário está logado no momento.")

def menu():
    biblioteca = Biblioteca()
    
    while True:
        print("\nMenu:")
        print("1. Adicionar Livro")
        print("2. Buscar Livro")
        print("3. Listar Livros")
        print("4. Emprestar Livro")
        print("5. Devolver Livro")
        print("6. Registrar Usuário")
        print("7. Login")
        print("8. Logout")
        print("9. Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            titulo = input("Título do livro: ")
            autor = input("Autor do livro: ")
            ano = input("Ano de publicação: ")
            biblioteca.adicionar_livro(titulo, autor, ano)
        
        elif escolha == '2':
            titulo = input("Título do livro (pressione Enter para pular): ")
            autor = input("Autor do livro (pressione Enter para pular): ")
            resultados = biblioteca.buscar_livro(titulo if titulo else None, autor if autor else None)
            if resultados:
                for livro in resultados:
                    print(f'Título: {livro.titulo}, Autor: {livro.autor}, Ano: {livro.ano}, Disponível: {"Sim" if livro.disponivel else "Não"}')
            else:
                print("Nenhum livro encontrado.")
        
        elif escolha == '3':
            biblioteca.listar_livros()
        
        elif escolha == '4':
            titulo = input("Título do livro a ser emprestado: ")
            biblioteca.emprestar_livro(titulo)
        
        elif escolha == '5':
            titulo = input("Título do livro a ser devolvido: ")
            biblioteca.devolver_livro(titulo)
        
        elif escolha == '6':
            nome = input("Nome: ")
            username = input("Username: ")
            senha = input("Senha: ")
            biblioteca.registrar_usuario(nome, username, senha)
        
        elif escolha == '7':
            username = input("Username: ")
            senha = input("Senha: ")
            biblioteca.login_usuario(username, senha)
        
        elif escolha == '8':
            biblioteca.logout_usuario()
        
        elif escolha == '9':
            break
        
        else:
            print("Opção inválida. Por favor, escolha novamente.")

# Inicializa o menu do sistema de biblioteca
menu()
