"""
SÉRIE DE EXERCÍCIOS 3 - Extra

Parte de um dos exercícios de revisão.
"""

def teste():
    soma = 0
    with open('extra.txt') as fich:
        for linha in fich:
            try:
                partes = linha.split()
                soma += float(partes[1])
            except ValueError:
                print("ERRO:", linha, end='')
            else:
                print(partes[0], '->', partes[1])
    print(soma)
