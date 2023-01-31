"""
LABORATÓRIO 2

Pretende fazer uma variação do comando tr (consultar man tr). Na sua 
forma mais geral, este clone, tr.py, recebe uma lista de padrões - SET1 - 
e uma lista de transformações - SET2 -, delimitadas em ambos os casos 
por : , e aplica-as por ordem. Um padrão é uma expressão regular aceite 
pelas funções do módulo re. Em alternativa pode utilizar o mais completo 
módulo regex, que não faz parte da biblioteca padrão. Uma transformação é 
uma sequência de uma ou mais palavras delimitada por : . Vejamos os 
seguinte exemplos:
"""

import sys
import re
from typing import TextIO
# pylint: disable=W0621

def tr(transforms: dict, file: TextIO=sys.stdin):
    for line in file:
        for old, new in transforms.items():
            line = tr_line(line, old, new)
        print(line, end='')


def tr_line(line: str, old: str, new: str) -> str:
    return re.sub(old, new, line)


# def tr_line(line: str, old: str, new: str) -> str:
#     pattern = re.compile(old)
#     return pattern.sub(new, line)


if __name__ == '__main__':
    from textwrap import dedent
    from docopt import docopt

    script_name = sys.argv[0].rpartition('/')[-1]
    doc = dedent(f"""
    Generalized TR clone. Replaces tokens filtered by the transformations
    in SET1 with the replacements in SET2.

    Usage: {script_name} SET1 SET2
           {script_name} -d SET1

    Options:
        -d, --delete    Delete tokens filtered by the transformations in SET1 
        -h, --help      This help
    """)

    args = docopt(doc)
    # print(args)
    old = args['SET1'].split(':')
    if args['--delete']:
        # generate len(old) empty transformations
        new = [''] * len(old)  
    else:
        new = args['SET2'].split(':')        
    tr(dict(zip(old, new)))
    # compiled_regexs = [re.compile(regex) for regex in old]
    # tr(dict(zip(compiled_regexs, new)))

