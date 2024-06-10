# ATIVIDADE 04 ORIENTAÇÃO A OBJETOS

# QUESTÃO 1
class Livro:
    livros=[]

    def __init__(self,titulo,autor,ano_publicacao):
        self._titulo=titulo
        self._autor=autor
        self._ano_publicacao=ano_publicacao        
        self._disponivel=True
        
        Livro.livros.append(self)    

# QUESTÃO 2

    def __str__(self):
        return f'Título do livro: {self._titulo} | Autor: {self._autor} | Ano de publicação: {self._ano_publicacao} | Disponível: {self._disponivel}'


# livro1=Livro('O número 1', 'Albert One', '1994')
# livro2=Livro('O número 2', 'Florence Two', '2005')

# print(livro1)
# print('')
# print(livro2)

# QUESTÃO 3

    @classmethod
    def listar_livros(cls):
        print(f'{'Título'.ljust(20)} | {'Autor'.ljust(20)} | {'Ano de publicação'.ljust(20)} | {'Disponível'}')
        for livro in cls.livros:
            print(f'{livro._titulo.ljust(20)} | {livro._autor.ljust(20)} | {livro._ano_publicacao.ljust(20)} | {livro.esta_disponivel}')

    @property
    def esta_disponivel(self):
        return 'Sim' if self._disponivel else 'Não'

    def emprestar_livro(self):
       self._disponivel=not self._disponivel

# livro2=Livro('O número 2', 'Florence Two', '2005')
# livro3=Livro('O número 3', 'Streve Three', '1986')

# Livro.listar_livros()

# print(f'O livro "{livro3._titulo}" está disponível? - {livro3.esta_disponivel}')

# QUESTÃO 4

    @staticmethod
    def verificar_disponibilidade(ano):
        livros_disponiveis = []
        for livro in Livro.livros:
            if livro._ano_publicacao == ano and livro._disponivel:
                livros_disponiveis.append(livro)
        return livros_disponiveis

    def anos():
        ano = input("Digite o ano para verificar disponibilidade dos livros: ")
        livros_disponiveis = Livro.verificar_disponibilidade(ano)
        if livros_disponiveis:
            print('')
            print("Livros disponíveis no ano", ano)
            for livro in livros_disponiveis:
                print(livro._titulo)
        else:
            print('')
            print("Nenhum livro disponível no ano", ano)

# livro1 = Livro('O número 1', 'Albert One', '1994')
# livro2 = Livro('O número 2', 'Florence Two', '2005')
# livro3 = Livro('O número 3', 'Streve Three', '1994')


# Livro.listar_livros()
# Livro.anos()
# QUESTÃO 5
    # CRIADO biblioteca.py 
# QUESTÃO 6
    # presente na biblioteca.py


# CURIOSIDADE
# @staticmethod
# for livro in livros_disponiveis:
    # print(f'Livros disponiveis em {ano}: {livro})
# Livro.livros=[livro1,livro2,livro3]