"""
SÉRIE DE EXERCÍCIOS 2

Pretendemos um programa que solicita um número ao utilizador e indica 
se esse número é primo (relembrando, um número é primo apenas se for 
divisível por 1 ou por ele próprio).
"""

num = int(input("Indique um numero: "))

# Versão com ciclo WHILE e sem BREAK
# i = 2
# primo = True
# while primo and i < num:
#     if num % i == 0:
#         primo = False
#     i += 1

primo = True if num >= 2 else False
for d in range(2, num):
    if num % d == 0:
        primo = False
        break        

if primo: 
    print("O número é primo")
else:
    print("O número não é primo")
