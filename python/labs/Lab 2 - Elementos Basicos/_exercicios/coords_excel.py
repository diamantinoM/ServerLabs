"""
Faça um programa para traduzir as coordenadas "simbólicas" do Excel 
para coordenadas lineares. Por exemplo, em Excel, internamente, a 
célula A1 corresponde à célula na linha 0 e coluna 2. Exemplos:

    Indique as coordenadas: Z 2 
    Linha: 1 Coluna: 25
    ---
    Indique as coordenadas: AA 3 
    Linha: 2 Coluna: 26
    ---
    Indique as coordenadas: AB 17 
    Linha: 16 Coluna: 27
    --
    Indique as coordenadas: CD 17 
    Linha: 16 Coluna: 81
    --
    Indique as coordenadas: sair 
    Fim do programa
"""

opcao = input("Indique as coordenadas: ")
while opcao != 'sair':
    col, lin = opcao.split()
    lin_number = int(lin) - 1

    col_number = -1
    for exp, letter in enumerate(reversed(col.upper())):
        letter_ordinal = ord(letter) - ord('A') + 1 
        col_number += letter_ordinal * (26 ** exp)

    print("Linha:", lin_number, "Coluna:", col_number)
    print("--")
    opcao = input("Indique as coordenadas: ")
