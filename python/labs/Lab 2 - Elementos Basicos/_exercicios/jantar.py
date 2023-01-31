"""
SÉRIE DE EXERCÍCIOS 2 

Um grupo de pessoas participou num jantar em que todos encomendaram o 
menu turístico e pretende fazer um programa para calcular a conta. 
Para tal, o programa deve comecar por ler o número de pessoas 
envolvidas no jantar e, de seguida, calcular o valor da conta. O menu 
custa 15,00 € + IVA por pessoa. Assuma que o IVA é 23% e a gorjeta 
para o empregado é de 10% sobre o montante total com IVA. O programa 
deve exibir a despesa total sem IVA e sem gorjeta, o montante de IVA, o
valor da gorjeta e a despesa total final.
"""

preco_menu = 15    # €
IVA        = 0.23  # 23%
gorjeta    = 0.10  # 10%

num_pessoas = int(input("Jantar para quantas pessoas? "))

despesa_s_iva = num_pessoas * preco_menu
montante_iva  = despesa_s_iva * IVA
despesa_c_iva = despesa_s_iva + montante_iva
montante_gorj = despesa_c_iva * gorjeta

print("Despesa S/ IVA:  {:.2f}€".format(despesa_s_iva))
print("Montante IVA:    {:.2f}€".format(montante_iva))
print("Despesa C/ IVA:  {:.2f}€".format(despesa_c_iva))
print("Gorjeta ({}%):   {:.2f}€".format(gorjeta, montante_gorj))
print()  
print("Despesa TOTAL:   {:.2f}€".format(despesa_c_iva + montante_gorj))
print()
