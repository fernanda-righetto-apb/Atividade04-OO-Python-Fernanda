# QUESTÃO 8
from modelo.livro import Livro

livro1 = Livro('O número 1', 'Albert One', '1994')
livro2 = Livro('O número 2', 'Florence Two', '2005')
livro3 = Livro('O número 3', 'Streve Three', '1994')

print(livro1)
print(livro3)
print('')
print('')


def main():
    Livro.listar_livros()

if __name__ =='__main__':
    main()