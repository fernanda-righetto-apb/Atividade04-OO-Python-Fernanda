# QUESTÃO 5 
# import da classe livro
from modelo.livro import Livro

livro1 = Livro('O número 1', 'Albert One', '1994')
livro2 = Livro('O número 2', 'Florence Two', '2005')
livro3 = Livro('O número 3', 'Streve Three', '1994')

# QUESTÃO 6
# livro2.emprestar_livro()
# print(f'O livro {livro2._titulo}, {livro2.esta_disponivel} está disponível!')
# print('')

# QUESTÃO 7
Livro.anos()

def main():
    Livro.listar_livros()

if __name__ =='__main__':
    main()