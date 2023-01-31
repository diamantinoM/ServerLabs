"""
SÉRIE DE EXERCÍCIOS 2

Agora faca um programa que utiliza o anterior e devolve todos os 
números primos até ao número introduzido pelo utilizador na linha 
de comandos.
"""

import sys
from primo3 import e_primo


if len(sys.argv) != 2:
    print("Utilização: python3", __file__, "N")

else:
    N = int(sys.argv[1])
    i = 1
    while i <= N:
        if e_primo(i):
            print(i)
        i += 1

    # no laboratório seguinte veremos que 
    # podemos fazer isto assim:
    # for i in range(1, N+1):
    #   if e_primo(i):
    #       print(i)
    #
    # ou
    #
    # print([i for i in range(1, N+1) if ePrimo(i)])
