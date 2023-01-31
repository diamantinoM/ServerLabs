"""
SÉRIE DE EXERCÍCIOS 2

Determina se um ano introduzido pelo utilizador é um ano
bissexto.

DADOS DE ENTRADA:
    ano: int

DADOS DE SAÍDA
    o ano é bissexto? : bool

    e_bissexto = multiplo de 400 ou nao_multiplo de 100 e multiplo de 4
"""
# pylint: disable=C0103

import sys

ano = int(input("Indique o ano: "))
if ano < 0:
    print(f"Ano inválido {ano}")
    sys.exit(1)

if ano % 400 == 0 or (ano % 100 != 0 and ano % 4 == 0):
    print("Bissexto")
else:
    print("Não bissexto")
