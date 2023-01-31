"""
SÉRIE DE EXERCÍCIOS 3

Faça um script que exibe um ficheiro de texto de forma paginada,
exibindo em cada linha o número da mesma, seguido do conteúdo da dita.
A exibição paginada deverá ser levada a cabo por uma função que recebe
o caminho do ficheiro e quantas linhas por página. Após cada página, o
programa deve aguardar que o utilizador pressione ENTER antes de
avançar para a próxima página.
"""

import sys
import os


LINHAS_PAGINA = 25


def exibe_fich(fich, linhas_pagina=LINHAS_PAGINA):
    with open(fich, 'r') as inf:
        for i, linha in enumerate(inf, 1):  # Ver NOTAS
            print("{:>03}| {}".format(i, linha), end='')
            if i % linhas_pagina == 0:
                input("Pressione ENTER para continuar...")
                cls()


def cls():
    if (sys.platform.startswith('linux') or
        sys.platform.startswith('darwin') or
        sys.platform.startswith('freebsd')):
        os.system('clear')
    elif sys.platform.startswith('windows'):
        os.system('cls')


def main():
    if not 2 <= len(sys.argv) <= 3:
        print("Utilização: python3", __file__, "fich [linhas_por_pag]")
    else:
        linhas_pagina = int(sys.argv[2]) if len(sys.argv) == 3 else LINHAS_PAGINA
        exibe_fich(sys.argv[1], linhas_pagina)


if __name__ == '__main__':
    main()


# NOTAS
# Podemos utilizar enumerate com file objects (se conseguimos
# iterar com FOR podemos utilizar ENUMERATE, SORTED e tudo o 
# que espera um iterável
