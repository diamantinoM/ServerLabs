"""
SÉRIE DE EXERCÍCIOS 2

Pretende fazer um programa em Python para gerar aleatoriamente grupos
de alunos para a realização de projectos e trabalhos de grupo. O seu 
script deve processar um ficheiro de entrada com os nomes dos alunos, 
um por linha, e gerar um ficheiro de saída para onde deve enviar a 
listagem dos grupos, um grupo por linha com os nomes separados por 
vírgulas. Deve também receber o número de elementos a agrupar. 
O script deve ser invocado de acordo a com a seguinte sintaxe:

$ python3 agrupa.py FICHEIRO_ENTRADA FICHEIRO_SAIDA NUM

"""

import sys
from random import shuffle


if len(sys.argv) != 4:
    print("Utilização: python3", sys.argv[0], "FICH_ENTRADA FICH_SAIDA NUM")
else:    
    fich_e = open(sys.argv[1], 'r')
    nomes = list(fich_e)
    fich_e.close()
    fich_s = open(sys.argv[2], 'w')
    dim_grupo = int(sys.argv[3])

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
