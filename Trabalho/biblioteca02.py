import pickle

class Livro:
    def __init__(self, titulo, autor, ano):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.disponivel = True

class Biblioteca:
    def __init__(self):
        self.livros = []
        self.carregar_dados()
        if not self.livros:  # Inicializa a biblioteca com alguns livros predefinidos
            self.inicializar_biblioteca()

    def inicializar_biblioteca(self):
        livros_predefinidos = [
            ("Código limpo", "Robert C. Martin", 2008 ),
            ("O Senhor dos Anéis", "J.R.R. Tolkien", 1954),
            ("O Programador pragmático", "Andy Hunt e Dave Thomas", 2010)
        ]
        for titulo, autor, ano in livros_predefinidos:
            self.adicionar_livro(titulo, autor, ano, inicializacao=True)
        self.salvar_dados()

    def salvar_dados(self):
        with open('biblioteca.pkl', 'wb') as f:
            pickle.dump(self.livros, f)

    def carregar_dados(self):
        try:
            with open('biblioteca02.pkl', 'rb') as f:
                self.livros = pickle.load(f)
        except FileNotFoundError:
            self.livros = []

    def adicionar_livro(self, titulo, autor, ano, inicializacao=False):
        for livro in self.livros:
            if livro.titulo.lower() == titulo.lower() and livro.autor.lower() == autor.lower():
                if not inicializacao:
                    print(f'O livro "{titulo}" já existe na biblioteca.')
                return
        novo_livro = Livro(titulo, autor, ano)
        self.livros.append(novo_livro)
        if not inicializacao:
            self.salvar_dados()
            print(f'Livro "{titulo}" adicionado com sucesso.')

    def buscar_livro(self, titulo):
        for livro in self.livros:
            if livro.titulo.lower() == titulo.lower():
                status = "Disponível" if livro.disponivel else "Emprestado"
                print(f'Título: {livro.titulo}, Autor: {livro.autor}, Ano: {livro.ano}, Status: {status}')
                return
        print(f'Livro "{titulo}" não encontrado na biblioteca.')

    def listar_livros(self):
        if not self.livros:
            print("Nenhum livro na biblioteca.")
        for livro in self.livros:
            status = "Disponível" if livro.disponivel else "Emprestado"
            print(f'Título: {livro.titulo}, Autor: {livro.autor}, Ano: {livro.ano}, Status: {status}')

    def emprestar_livro(self, titulo):
        for livro in self.livros:
            if livro.titulo.lower() == titulo.lower() and livro.disponivel:
                livro.disponivel = False
                self.salvar_dados()
                print(f'Livro "{titulo}" emprestado com sucesso.')
                return
        print(f'Livro "{titulo}" não está disponível para empréstimo.')

    def devolver_livro(self, titulo):
        for livro in self.livros:
            if livro.titulo.lower() == titulo.lower() and not livro.disponivel:
                livro.disponivel = True
                self.salvar_dados()
                print(f'Livro "{titulo}" devolvido com sucesso.')
                return
        print(f'Livro "{titulo}" não foi encontrado como emprestado.')

def menu():
    biblioteca = Biblioteca()
    
    while True:
        print("\nMenu:")
        print("1. Adicionar Livro")
        print("2. Buscar Livro")
        print("3. Listar Livros")
        print("4. Emprestar Livro")
        print("5. Devolver Livro")
        print("6. Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            titulo = input("Título do livro: ")
            autor = input("Autor do livro: ")
            ano = input("Ano de publicação: ")
            biblioteca.adicionar_livro(titulo, autor, ano)
        
        elif escolha == '2':
            titulo = input("Título do livro: ")
            biblioteca.buscar_livro(titulo)
        
        elif escolha == '3':
            biblioteca.listar_livros()
        
        elif escolha == '4':
            titulo = input("Título do livro a ser emprestado: ")
            biblioteca.emprestar_livro(titulo)
        
        elif escolha == '5':
            titulo = input("Título do livro a ser devolvido: ")
            biblioteca.devolver_livro(titulo)
        
        elif escolha == '6':
            break
        
        else:
            print("Opção inválida. Por favor, escolha novamente.")

# Inicializa o menu do sistema de biblioteca
menu()
