"""
SÉRIE DE EXERCÍCIOS 2 

Faça um programa para ler texto, caractere a caractere, até que o 
utilizador introduza o caractere . (ponto). No final deverá indicar 
quantos digítos e espaços o utilizador inseriu.
"""

DIGITOS = "0123456789"

ndigitos = nespacos = 0
ler_linha = True
while ler_linha:
    linha = input()
    for ch in linha:
        if ch == '.':
            ler_linha = False
            break
        ndigitos += 1 if ch in DIGITOS else 0
        nespacos += 1 if ch == ' ' else 0

print(
    "Espaços: %s" % nespacos,
    "Dígitos: %s" % ndigitos,
    sep='\n', 
)
