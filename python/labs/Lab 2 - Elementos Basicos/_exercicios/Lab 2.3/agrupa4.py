#!/usr/bin/env python3 
"""
SÉRIE DE EXERCÍCIOS 2

Pretende fazer um programa em Python para gerar aleatoriamente grupos
de alunos para a realização de projectos e trabalhos de grupo. O seu 
script deve processar um ficheiro de entrada com os nomes dos alunos, 
um por linha, e gerar um ficheiro de saída para onde deve enviar a 
listagem dos grupos, um grupo por linha com os nomes separados por 
vírgulas. Deve também receber o número de elementos a agrupar. 

Esta versão utiliza o módulo docopt e é invocada com as seguintes
sintaxes:

$ python3 agrupa.py [-i FICHEIRO_ENTRADA] [-o FICHEIRO_SAIDA] [-n NUM]
$ python3 agrupa.py [--in=FICHEIRO_ENTRADA] [--out=FICHEIRO_SAIDA] [--num=NUM]

Esta versão prepara também o script para ser importado por outros 
scripts. Para tal, colocamos o código que lida com a linha de comandos
(ie, com a parte "executável" do script) debaixo de um 
"if __name__ == '__main__'". Definimos também uma função para 
agrupar os linhas do ficheiro de entrada e produzir o ficheiro 
de saída
"""

import sys
from random import shuffle


def agrupa_linhas(fich_e, fich_s, dim_grupo):   # (*)
    fich_e = open(fich_e, 'r') if fich_e else sys.stdin
    nomes = list(fich_e)
    fich_e.close()
    fich_s = open(fich_s, 'w') if fich_s else sys.stdout

    shuffle(nomes)
    for i in range(0, len(nomes), dim_grupo):
        nomes_por_linha = []  # (*)
        for nome in nomes[i:i + dim_grupo]:
            nomes_por_linha.append(nome.strip())
        fich_s.write(', '.join(nomes_por_linha))
        fich_s.write('\n')

    fich_s.close()


if __name__ == '__main__':
    from docopt import docopt
    from textwrap import dedent
    doc = r"""
    Agrupa linhas de ficheiro.

    Usage:
    agrupa.py [-i FICHEIRO_ENTRADA] [-o FICHEIRO_SAIDA] [-n NUM]
    agrupa.py [--in=FICHEIRO_ENTRADA] [--out=FICHEIRO_SAIDA] [--num=NUM]

    Options:
    -h --help                                   Mostra a ajuda.
    --in=FICHEIRO_ENTRADA, -i FICHEIRO_ENTRADA  Ficheiro de entrada
    --out=FICHEIRO_SAIDA, -o FICHEIRO_SAIDA     Ficheiro de saída
    --num=NUM, -n NUM                           Número de elementos por linha [default: 2]
    """
    args = docopt(dedent(doc), version='Versão 1')
    agrupa_linhas(args['--in'], args['--out'], int(args['--num']))

