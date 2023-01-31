"""
SÉRIE DE EXERCÍCIOS 2 

Faça um programa de adivinha que pede um número ao utilizador (o número 
mágico) e indica se ele acerta qual é o número mágico (eg, 19). O 
programa termina quando o utilizador acertar e, em cada tentativa, deve 
indicar se o utilizador está próximo ou muito próximo.
"""
from random import randint

num_magico = randint(1, 30)
DIF_PROXIMA = 2
DIF_MUITO_PROXIMA = 1

while True:
    num = int(input("\nQual o número mágico? "))
    dif = abs(num_magico - num) 

    if dif == 0:
        print("Parabéns, acertou")
        break
    elif dif <= DIF_MUITO_PROXIMA:
        print("Falhou, mas está _muito_ perto de acertar!")
    elif dif <= DIF_PROXIMA:
        print("Falhou, mas está perto de acertar!")
    else:
        print("Falhou.")

    if input("\nDeseja repetir? ").upper() in ('N', 'NÃO'):
        break

