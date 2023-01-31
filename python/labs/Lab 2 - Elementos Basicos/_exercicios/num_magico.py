"""
DEFINIÇÃO DO PROBLEMA:
Programa de adivinha. O utilizador deve adivinhar um número
e dispõe de várias tentativas para o fazer

DESCRIÇÃO DO PROBLEMA:
O programa começa por gerar um número aleatório entre 0 e 20.
Depois pede ao utilizador para tentar adivinhar. Se o utilizador
acertar o programa termina. Se não acertar, o programa indica
a proximidade da tentativa e volta a solicitar uma nova tentativa.

DADOS ENTRADA:
    num_magico -> número aleatório entre 0 e 20, int
                  obtido com random.randint
    num        -> número introduzido pelo do utilizador (tentativa), int                

DESENHO DA SOLUÇÃO:
    Fluxograma à parte

DADOS SAÍDA
    Exibe na saída padrão o seguinte:
        Acertou       -> caso o utilizador tenha acertado
        Próximo       -> caso esteja a 3 valores de "distância"
        Muito próximo -> caso esteja a 1 valor de "distância"
"""

from random import randint

num_magico = randint(0, 20)
dist = -1
while dist != 0:
    num = int(input("Adivinhe o número mágico? "))
    dist = abs(num_magico - num)
    
    if dist == 0:
        print("Acertou")
    elif dist <= 1:
        print("Muito próximo!")
    elif dist <= 3:
        print("Próximo!")
    else:
        print("Falhou")