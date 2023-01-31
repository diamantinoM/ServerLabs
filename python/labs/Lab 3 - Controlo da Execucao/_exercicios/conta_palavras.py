"""
SÉRIE DE EXERCÍCIOS 3

Faça um programa para contar as palavras introduzidas na entrada 
padrão. Entende-se por palavra uma sequência de letras sem espaços. 
"""

import sys


def conta_palavras(txt):
    n_palavras = 0
    for pseudo_palavra in txt.split():
        if pseudo_palavra.isalpha():
            n_palavras += 1
    return n_palavras

# Com expressões geradoras fica mais fácil:
# 
# def conta_palavras(txt):
#     return sum(pseudo_palavra.isalpha() for pseudo_palavra in txt.split())

def main1():
    """
    Este `main` lê linhas da entrada padrão até encontrar uma linha 
    vazia (com 0 caracteres). 
    """
    n_palavras = 0
    while True:
        linha = input()
        if not linha:
            break
        n_palavras += conta_palavras(linha)
    print("Número de palavras ->", n_palavras)


def main2():
    """
    Este `main` lê a entrada como se de um ficheiro de texto se 
    tratasse. 

    NOTA: também podíamos utilizar o `input` para ler a entrada
    padrão como se um ficheiro se tratasse, mas aí o final de 
    ficheiro é sinalizado com uma excepção. 
    """
    n_palavras = 0
    for linha in sys.stdin:
        n_palavras += conta_palavras(linha)
    print("Número de palavras ->", n_palavras)


if __name__ == '__main__':
    main2()