"""
SÉRIE DE EXERCÍCIOS 2 

Por vezes é útil obter mudar o endereço MAC de um adaptador de rede 
(eg, para contornar um switch que bloqueia portas a um determinado
MAC). Utilizando as funcionalidades do módulo random, tente fazer um 
programa que gera um MAC address válido de forma aleatória. 
"""

from random import choice


HEX_DIGITS = "0123456789ABCDEF"

mac  = choice(HEX_DIGITS) + choice(HEX_DIGITS) + ':'
mac += choice(HEX_DIGITS) + choice(HEX_DIGITS) + ':'
mac += choice(HEX_DIGITS) + choice(HEX_DIGITS) + ':'
mac += choice(HEX_DIGITS) + choice(HEX_DIGITS) + ':'
mac += choice(HEX_DIGITS) + choice(HEX_DIGITS) + ':'
mac += choice(HEX_DIGITS) + choice(HEX_DIGITS)

print(mac)