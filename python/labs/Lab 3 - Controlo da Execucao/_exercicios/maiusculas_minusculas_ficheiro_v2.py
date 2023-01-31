"""
SÉRIE DE EXERCÍCIOS 3

Faça um script que recebe pela linha de comandos o caminho para um 
ficheiro de texto e copia para outro ficheiro de texto, o texto 
original mas com as letras maiúsculas convertidas em minúsculas.
O script deve ser invocado assim:
  $ python3 [-if input_file] [-of output_file]
"""

import sys
from argparse import ArgumentParser    


def copy_txt_file(inf, outf):
    for line in inf:
        # cada linha já vem com '\n'
        outf.write(line.lower())


def main():
    parser = ArgumentParser(description="Copy text file")
    parser.add_argument(
        '-if',
        help="Input file",
        metavar="input_file",
        required=False,
        dest='if_',
    )
    parser.add_argument(
        '-of',
        help="Output file",
        metavar="output_file",
        required=False,
    )
    args = parser.parse_args()

    # Neste caso, com excepções poderiamos fazer código mais simples,
    # mas ainda não chegámos lá... 
    # Gestores de contexto com @contextmanager também poderiam 
    # simplificar o código. 

    if args.if_ and args.of:
        with open(args.if_, 'r') as inf:
            with open(args.of, 'w') as outf:
                copy_txt_file(inf, outf)
    elif args.if_:
        with open(args.if_, 'r') as inf:
            copy_txt_file(inf, sys.stdout)
    elif args.of:
        with open(args.of, 'w') as outf:
            copy_txt_file(sys.stdin, outf)
    else:
        copy_txt_file(sys.stdin, sys.stdout)


if __name__ == '__main__':
    main()

