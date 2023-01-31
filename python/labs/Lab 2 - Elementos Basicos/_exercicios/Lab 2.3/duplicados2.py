"""
SÉRIE DE EXERCÍCIOS 2 

Vamos agora fazer um programa para detectar ficheiros idênticos, isto é,
ficheiros cujo conteúdo é igual. Através da linha de comandos, o seu 
programa recebe um caminho para uma directoria e no final deve exibir 
uma listagem com todos os ficheiros duplicados dentro dessa directoria, 
inclusive dentro das sub-directorias.

Sugestões:

1. Pode utilizar os.walk para percorrer árvore de directorias dentro 
   do caminho fornecido

2. Pode utilizar hashlib.md5 para obter de forma eficiente um resumo 
   de cada ficheiro. Este resumo é unívoco, isto é, dois ficheiros com 
   conteúdo igual produzem um resumo igual; dois ficheiros com conteúdo 
   diferente (mesmo que ligeiramente diferente) produzem um resumo 
   diferente

3. Pode utilizar um dicionário para guardar estes resumos e listar, por
   cada resumo, o nome dos ficheiros que produziram esse resumo
"""

import os
import sys
from hashlib import md5
from pprint import pprint


def print_duplicates(path_):
    files = {}  # assinatura -> ficheiros com essa assinatura
    for dirpath, dirnames, filenames in os.walk(path_):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            with open(file_path, 'rb') as f:
                hash_ = md5(f.read()).hexdigest()
            files.setdefault(hash_, []).append(file_path)

    for names in files.values():
        if len(names) > 1:
            pprint(names)


if __name__ == '__main__':
    path_ = '.' if len(sys.argv) == 1 else sys.argv[1]
    print_duplicates(path_)


