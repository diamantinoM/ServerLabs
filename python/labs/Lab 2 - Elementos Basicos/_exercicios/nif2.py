"""
SÉRIE DE EXERCÍCIOS 2 

Programa que verifica se um número introduzido pelo utilizador
é um NIF válido. Nesta versão utilizámos um ciclo WHILE no 
algoritmo de validação (sem grande vantagem, quanto a mim...)

Regras de validação:
O NIF tem 9 dígitos, sendo o último o digito de controlo. Para ser 
calculado o digito de controlo:

1. Multiplique o 8.º dígito por 2, o 7.º dígito por 3, o 6.º dígito 
   por 4, o 5.º dígito por 5, o 4.º dígito por 6, o 3.º dígito por 7, 
   o 2.º dígito por 8, e o 1.º digito por 9
2. Adicione os resultados
3. Calcule o Módulo 11 do resultado, isto é, o resto da divisão do 
   número por 11.
4. Se o resto for 0 ou 1, o dígito de controle será 0
5. Se for outro algarismo x, o dígito de controle será o resultado 
   de 11 - x
"""

import sys


def is_nif(num_str):
    if len(num_str) != 9 or not num_str.isdigit():
        return False

    resultado = 0
    for i in range(8):
        resultado += int(num_str[i]) * (9 - i)

    # i = resultado = 0
    # while i <= 7:
    #     resultado += int(num_str[i]) * (9 - i)
    #     i += 1
        
    resultado %= 11
    digito_controlo = int(num_str[8])

    if resultado in (0, 1):
        return digito_controlo == 0
    else:
        return digito_controlo == 11 - resultado

    # Ou ...
    # return digito_controlo == 0 if resultado in (0, 1) else \
    #        digito_controlo == 11 - resultado


if __name__ == '__main__':
    if len(sys.argv) > 2:
        print("Utilização: python3", __file__, "[num]")
    else:
        if len(sys.argv) == 2:
            num = sys.argv[1]
        else:
            num = input("Introduza um NIF para verificação: ")

        print("NIF válido" if is_nif(num) else "NIF inválido")

