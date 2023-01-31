"""
SÉRIE DE EXERCÍCIOS 2 

Por vezes é útil obter mudar o endereço MAC de um adaptador de rede (eg, 
para contornar um switch que bloqueia portas a um determinado MAC). 
Utilizando as funcionalidades do módulo hashlib (por exemplo) e um dos 
algoritmos de resumo (digest), tente fazer um programa que gera um MAC 
address válido de forma aleatória. 
"""

from hashlib import md5
from random import randint


resumo = md5()
resumo.update(str(randint(1, 100000)).encode())
mac = resumo.hexdigest()[:12]
#print(mac)

pares = []
for i in range(0, len(mac), 2):
    pares.append(mac[i:i+2])
print(':'.join(pares))

# pares = []
# i = 0
# while i < len(mac):
#     pares.append(mac[i:i+2])
#     i += 2
# print(':'.join(pares))
''
# pares = []
# for h1, h2 in zip(mac[0::2], mac[1::2]):
#     pares.append(h1 + h2)
# print(':'.join(pares))

# pares = map(''.join, zip(mac[0::2], mac[1::2]))
# print(':'.join(pares))

# print(':'.join(map(''.join, zip(mac[0::2], mac[1::2]))))

# print(':'.join(h1 + h2 for h1, h2 in zip(mac[0::2], mac[1::2])))
