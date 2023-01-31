"""
SÉRIE DE EXERCÍCIOS 3

Faça um script que recebe pela linha de comandos o caminho para um 
ficheiro de texto e exibe (na saída padrão) o texto com as letras 
maiúsculas convertidas em minúsculas.
"""

import sys


def main():
    if len(sys.argv) != 2:
        print("Utilização: python3", __file__, "fich")
    else:
        with open(sys.argv[1], 'r') as fich:
            for line in fich:
                # cada linha já vem com '\n'
                print(line.lower(), end='')


if __name__ == '__main__':
    main()

