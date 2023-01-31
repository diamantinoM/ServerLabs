"""
SÉRIE DE EXERCÍCIOS 2

Pretende fazer um programa em Python para gerar aleatoriamente grupos
de alunos para a realização de projectos e trabalhos de grupo. O seu 
script deve processar um ficheiro de entrada com os nomes dos alunos, 
um por linha, e gerar um ficheiro de saída para onde deve enviar a 
listagem dos grupos, um grupo por linha com os nomes separados por 
vírgulas. Deve também receber o número de elementos a agrupar. 

Esta versão utiliza o módulo argparse e é invocada com a seguinte
sintaxe:

$ python3 agrupa.py [-in FICHEIRO_ENTRADA] [-out FICHEIRO_SAÍDA] [-n NUM]

"""

import sys
import argparse
from random import shuffle


parser = argparse.ArgumentParser(description="Agrupa linhas de ficheiro")
parser.add_argument(
    '-in', '--input',
    metavar='FICHEIRO_ENTRADA',
    help='ficheiro de entrada',
)
parser.add_argument(
    '-out', '--output',
    metavar='FICHEIRO_SAIDA',
    help='ficheiro de saída',
)
parser.add_argument(
    '-n',
    metavar='NUM',
    help='número de elementos por linha',
    type=int,
    default=2,
)
args = parser.parse_args()


fich_e = open(args.input, 'r') if args.input else sys.stdin
nomes = list(fich_e)
fich_e.close()
fich_s = open(args.output, 'w') if args.output else sys.stdout
dim_grupo = args.n

shuffle(nomes)
for i in range(0, len(nomes), dim_grupo):
    nomes_por_linha = []  # (*)
    for nome in nomes[i:i + dim_grupo]:
        nomes_por_linha.append(nome.strip())
    fich_s.write(', '.join(nomes_por_linha))
    fich_s.write('\n')

fich_s.close()


# (*) de futuro, com expressões lista:
#  nomes_por_linha = [nome.strip() for nome in nomes[i:i+dim_grupo]]
#
# ou, com expressões geradoras:
#  nomes_por_linha = (nome.strip() for nome in nomes[i:i+dim_grupo])
# esta última versão é mais eficiente pq não gera uma lista temporária
# 
# ou passando a expressão geradora para dentro do join:
#  fich_s.write(', '.join(nome.strip() for nome in nomes[i:i+dim_grupo]))
