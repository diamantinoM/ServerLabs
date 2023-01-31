"""
SÉRIE DE EXERCÍCIOS 2

Faca um programa para calcular o preco de venda final de um produto.
Para tal solicita, através da linha de comandos (shell), o preço do 
produto, o valor da taxa de IVA a aplicar e (opcionalmente) o valor 
de um desconto a aplicar ao valor final do produto. O programa deverá
dar instruções ao utilizador de como deve ser invocado. O valor do IVA 
e do desconto deve ser dado em percentagem.
"""

# pylint: disable=C0103

import sys
from decimal import Decimal


if not 3 <= len(sys.argv) <= 4:
    print("Utilização: python3", __file__, "preco_sem_iva taxa_iva [desconto]")

else:
    preco_s_iva = Decimal(sys.argv[1])
    taxa_iva    = Decimal(sys.argv[2])
    desconto    = Decimal(sys.argv[3]) if len(sys.argv) == 4 else 0

    preco = preco_s_iva * ((100 + taxa_iva) / 100)
    preco_final = preco * ((100 - desconto) / 100)

    print("Preço final: {:.2f}".format(preco_final))

