import datetime 
from typing import Union 


# classe Date
#   + construtores:
#       o __init__ : ano, mes, dia, tem que ser validados (não aceitar 31/4,
#                    29/2/2019, ); lançar excepção do tipo InvalidDateValues que 
#                    deve derivar de ValueError
#       o construtor: data no formato AAAA-MM-DD
#       o construtor: data como inteiro (juliano) AAAAMMDD
#   + acessores:
#       o year, month, day (properties)
#   + predicados ("acessor" booleano):
#       o is_leap_year
#   + __str__ : mostra data 'AAAA-MM-DD'
#   + __repr__: mostra 'Date(ano, mês, dia)'
#   + outros métodos:
#       o __add__  : nova data igual a data + dias (int)
#       o __radd__ : nova data igual a dias (int) + data
#       o __sub__  : dias (int) que resultam de data - data
#       * NOTA: usar módulo datetime para fazer as contas com datas

class InvalidDateValues(ValueError):
    pass

