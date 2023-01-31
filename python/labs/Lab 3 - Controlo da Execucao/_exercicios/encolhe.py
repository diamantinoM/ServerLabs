#!/usr/bin/env python3

"""
SÉRIE DE EXERÍCIOS 3

Compressor que utiliza a biblioteca zipfile.
"""

import sys
import os
import os.path as ospath
import zipfile
from docopt import docopt
from textwrap import dedent


def main(argv):
    script_name = argv[0].rpartition(ospath.sep)[2]
    doc = """
    Compressor ZIP, BZIP2 e LZMA.

    Usage:
      {0} [(-z | -b | -l)] <arquivo> <caminho>...
      
    Options:
      -h --help      Mostra a ajuda.
      <arquivo>      Arquivo com extensão .ZIP
      <caminho>...   Uma sequência de caminhos para ficheiros individuais ou directorias
      -z             Comprime utilizando o algoritmo padrão do formato ZIP (ZIP_DEFLATED)
      -b             Comprime utilizando o algoritmo Burrows-Wheeler (BZIP2)
      -l             Comprime utilizando o algoritmo Lempel–Ziv–Markov chain (LZMA/7Z)
      -v --version   Mostra a versão.
    """.format(script_name)
    args = docopt(dedent(doc), version='Versão 1')
    
    # Nome de arquivo não pode ser uma directoria. Obtem nome do arquivo 
    # e acrescenta extensão zip se a última extensão não for zip.
    zip_file = args['<arquivo>']
    if zip_file != ospath.basename(zip_file):
        print("<arquivo> deve ser um ficheiro e não uma pasta.")
        sys.exit(1)

    zip_name, dot, zip_ext = zip_file.rpartition('.')
    zip_file = zip_file if zip_ext == 'zip' else zip_file + '.zip'

    # Determina algoritmo de compressão
    comp_algs = {
        '-z': zipfile.ZIP_DEFLATED,
        '-b': zipfile.ZIP_BZIP2,
        '-l': zipfile.ZIP_LZMA,
    }
    comp_args = (comp_arg 
                 for comp_arg in args 
                 if args[comp_arg] and comp_arg in comp_algs)
    comp_alg = comp_algs[next(comp_args, '-z')]

    # Cria arquivo e comprime caminhos para dentro do arquivo. Todos os
    # caminhos são prefixados com o nome do arquivo de modo a que do 
    # 'unzip' resulte uma directoria com o nome do arquivo.
    with zipfile.ZipFile(zip_file, 'w', comp_alg) as zipf:                
        for path in args['<caminho>']:
            if ospath.isdir(path): 
                zip_path = make_zip_path(zip_name, ospath.basename(path))
                zipdir(zipf, path, zip_path)
            else:
                zip_path = make_zip_path(zip_name, path)
                zipf.write(path, zip_path)


def zipdir(ziph, path, zip_path):
    """
    Adaptado daqui: 
    http://stackoverflow.com/questions/1855095/
          /how-to-create-a-zip-archive-of-a-directory
    """
    for root, dirs, files in os.walk(path):
        for file_ in files:
            ziph.write(ospath.join(root, file_), 
                       ospath.join(zip_path, file_))


def make_zip_path(zip_name, path):
    assert zip_name and path    
    return zip_name + path if ospath.isabs(path) else ospath.join(zip_name, path) 


if __name__ == '__main__':
    main(sys.argv)
