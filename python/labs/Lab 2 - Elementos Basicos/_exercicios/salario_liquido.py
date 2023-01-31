"""
SÉRIE DE EXERCÍCIOS 2 

Fazer um programa para calcular a contribuição para a Seguranca Social, 
IRS e o sindicato a partir do salario bruto, que é um atributo de 
entrada.
"""

from decimal import Decimal

SS   = Decimal('11.5')  # %
IRS  = Decimal('25')  # %
SIND = Decimal('0.5') # %

salario_bruto = Decimal(input("Qual o valor do salario bruto? "))

parcela_ss   = salario_bruto * (SS/100)
parcela_irs  = salario_bruto * (IRS/100)
parcela_sind = salario_bruto * (SIND/100)
salario_liq  = salario_bruto - parcela_ss - parcela_irs - parcela_sind


print("Contribuição Seg. Social: {:.2f}€".format(parcela_ss))
print("Montante IRS:             {:.2f}€".format(parcela_irs))
print("Contribuição Sindicato:   {:.2f}€".format(parcela_sind))
print()
print("Salário Líquido:          {:.2f}€".format(salario_liq))
print()

