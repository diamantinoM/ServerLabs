"""
SÉRIE DE EXERCÍCIOS 2

Vamos agora fazer um programa que lê três valores introduzidos na linha
de comandos e indica o maior deles.
"""
# pylint: disable=C0103

import sys

if len(sys.argv) != 4:
    print("Utilização: python3", sys.argv[0], "num1 num2 num3")

else:
    num1 = int(sys.argv[1])
    num2 = int(sys.argv[2])
    num3 = int(sys.argv[3])

    if num1 > num2 and num1 > num3:
		print(num1)
	elif num2 > num1 and num2 > num3: # bastava "elif num1 > num3:""
		print(num2)
	else:
		print(num3)
