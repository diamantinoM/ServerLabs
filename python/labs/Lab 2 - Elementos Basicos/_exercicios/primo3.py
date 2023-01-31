"""
SÉRIE DE EXERCÍCIOS 2

Pretendemos um programa que solicita um número ao utilizador e indica 
se esse número é primo (relembrando, um número é primo apenas se for 
divisível por 1 ou por ele próprio).

Este programa é uma versão adaptada de 'primo.py' de modo a que possa 
ser importado por outro módulo (necessário para o exercício que indica 
todos os primos).
"""

def e_primo(num):
    if num < 2:
        return False
    for d in range(2, num): 
        if num % d == 0:
            return False
    return True


if __name__ == '__main__':
    num = int(input("Indique um numero: "))

    if e_primo(num):             
        print("O número é primo")
    else:
        print("O número não é primo")
