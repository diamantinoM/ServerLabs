"""
SÉRIE DE EXERCÍCIOS 3

Pretende gerar uma lista com 10.000 tuplos com o seguinte conteúdo:
[(0, 0, 0, 0), (0, 0, 0, 1), (0, 0, 0, 2), ..., (9, 9, 9, 9)]
"""

def primeira_solucao():
    tuplos = []
    for i in range(10):
        for k in range(10):
            for j in range(10):
                for p in range(10):
                    tuplos.append((i, k, j, p))
    return tuplos


def segunda_solucao():
    tuplos = []
    for i in range(10000):
        tuplos.append(tuple("{:04}".format(i)))
    return tuplos


def terceira_solucao():
    tuplos = []
    for i in range(10000):
        tuplo_str = tuple("{:04}".format(i))
        tuplos.append((
            int(tuplo_str[3]), 
            int(tuplo_str[2]),
            int(tuplo_str[1]),
            int(tuplo_str[0]),
        ))
    return tuplos

# Com list comprehensions fica mais fácil
# 
# def terceira_solucao():
#     return [tuple("{:04}".format(i)) for i in range(10000)]

# Com itertools.product é canja
#
# from itertools import product
# def terceira_solucao():
#     return list(product(range(10), repeat=4))

# def solucao_pedro_mendes():
#     return [
#         (i, k, j, p) 
#         for i in range(10)
#         for k in range(10)
#         for j in range(10)
#         for p in range(10)
#     ]
