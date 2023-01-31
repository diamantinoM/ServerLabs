"""
Este programa calcula o preço de um produto aplicando IVA
e um desconto opcional. O programa é completamente
interactivo, isto é, a informação necessário é introduzida
por um utilizador de um programa.
"""

# pylint: disable=C0103

preco = float(input("Preco        : "))
taxa_iva = float(input("Taxa iva (%) : "))
desconto = input("Desconto (%) : ")
if desconto:
    desconto = float(desconto)
else:
    desconto = 0.0

preco_sem_desc = preco * (1 + taxa_iva/100)
preco_final = preco_sem_desc * (1 - desconto/100)
print(f"Preço final  : {preco_final:.2f}")


# desconto = input("Desconto (%) : ")
# desconto = float(desconto) if desconto else 0.0

# if desconto:
#     desconto = float(desconto)
# else:
#     desconto = 0.0
