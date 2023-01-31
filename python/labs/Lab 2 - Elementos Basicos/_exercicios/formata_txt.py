"""
SÉRIE DE EXERCÍCIOS 2 

Desenvolva um programa que recebe texto através da entrada padrão e 
formata-o a X colunas. Leia todo o texto da entrada padrão através 
do método sys.stdin.read (que veremos na próxima parte do 
laboratório). Utilize o módulo textwrap para formatar o texto. 
"""

import sys
from textwrap import fill


if len(sys.argv) != 2:
    print("Utilização: python3", sys.argv[0], "<NUM_COLUNAS>")
else:
    txt = sys.stdin.read()
    print(fill(txt, int(sys.argv[1])))


