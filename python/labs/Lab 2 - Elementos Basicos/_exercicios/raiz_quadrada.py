"""
SÉRIE DE EXERCÍCIOS 2 

Faça um programa para calcular a raiz quadrada de um número de acordo 
com o seguinte algorítmo genérico:

Algoritmo: Cálculo da Raiz Quadrada
  Entrada: N -> número real
    Saída: r -> número tal que r * r ~= N

1. Escolher um número arbitrário `r` entre 1 e N
2. Se N - e <= r*r <= N + e, com `e` muito pequeno
   (eg, 0,000000001) então o resultado é `r`.
3. Senão, fazer r = (r + N/r)/2
4. Voltar ao passo 2
"""

from random import uniform

E = 0.00000001


def sqrt_(N):
    assert N >= 0
    r = uniform(0, N)
    while True:
        if abs(N - r*r) <= E:
            return r
        r = (r + N/r) / 2


def main():
    print("Introduza CTRL+C/D ou um número negativo para terminar")
    while True:
        num = float(input('raiz> '))
        if num < 0:
            break
        print(sqrt_(num))


if __name__ == '__main__':
    main()
        


