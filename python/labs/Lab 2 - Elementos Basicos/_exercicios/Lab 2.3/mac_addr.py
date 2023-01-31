"""
SÉRIE DE EXERCÍCIOS 2 

Por vezes é útil obter mudar o endereço MAC de um adaptador de rede 
(eg, para contornar um switch que bloqueia portas a um determinado
MAC). Utilizando as funcionalidades do módulo random, tente fazer um 
programa que gera um MAC address válido de forma aleatória. 
"""

from random import choice

hex_digits = "0123456789ABCDEF"
pares = []
for i in range(6):
    pares.append(choice(hex_digits) + choice(hex_digits))
print(':'.join(pares))

# Depos de falarmos de list comprehensions
# print(':'.join([choice(hex_digits) + choice(hex_digits) for i in range(6)]))

# Mas fica melhor com generator expressions (não há necessidade listas)
# print(':'.join(choice(hex_digits) + choice(hex_digits) for i in range(6)))