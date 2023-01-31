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
    import argparse
    
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
    agrupa_linhas(args.input, args.output, args.n)


# (*) de futuro definiremos esta função de forma diferente