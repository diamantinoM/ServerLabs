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
            # Lê ficheiro e obtém um resumo (ie, uma assinatura)
            file_path = os.path.join(dirpath, filename)
            with open(file_path, 'rb') as f:
                hash_ = md5(f.read()).hexdigest()
            # Obtém entrada para este resumo e acrescenta nome do ficheiro.
            files_for_hash = files.get(hash_, [])
            files_for_hash.append(file_path)        
            files[hash_] = files_for_hash

    for names in files.values():
        if len(names) > 1:
            pprint(names)


if __name__ == '__main__':
    path_ = '.' if len(sys.argv) == 1 else sys.argv[1]
    print_duplicates(path_)


# A exibição pode ser simplificada com uma `list comprehension` 
# conforme veremos a seguir:
#     pprint([names for names in files.values() if len(names) > 1])

# Veremos no laboratório seguinte que cada ficheiro deve ser aberto 
# com um gestor de contexto através da palavra-reservada with
#
# files = {} # assinatura -> ficheiros com essa assinatura
# for dirpath, dirnames, filenames in os.walk(path_):
#    for filename in filenames:
#        file_path = os.path.join(dirpath, filename)
#        with open(file_path, 'rb') as f:
#            hash_ = md5(f.read()).hexdigest()
#        files_for_hash = files.get(hash_, [])
#        files_for_hash.append(file_path)        
#        files[hash_] = files_for_hash

# Os dicionários suportam uma operação que é o setdefault que permite
# inicializar o valor de uma entrada caso essa entrada não exista. 
# Um dos valores, o antigo valor, se a entrada já existir, ou o novo 
# valor de inicialização, é devolvido.
#
# files = {} # assinatura -> ficheiros com essa assinatura
# for dirpath, dirnames, filenames in os.walk(path_):
#     for filename in filenames:
#         file_path = os.path.join(dirpath, filename)
#         with open(file_path, 'rb') as f:
#            hash_ = md5(f.read()).hexdigest()
#         files.setdefault(hash_, []).append(file_path)
