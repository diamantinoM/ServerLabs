"""
DEFINIÇÃO DO PROBLEMA:
Dado o valor do salário bruto, este programa discrimina os montantes
para a Segurança Social, IRS e para um determinado sindicato.

DESCRIÇÃO DO PROBLEMA:
O programa recebe o salário bruto a partir da entrada padrão e depois
calcula e exibe de forma amigável os seguintes valores:
- Contribuição para a SS
- Impostos retidos em sede de IRS
- Contribuição para o sindicato
- Salário liquído resultante

ENTRADAS:
salario_bruto -> Salário sem descontos, tipo de dados: decimal.Decimal

Os seguintes parâmetros são constantes para este programa:
TAXA_SS         -> Contribuição do trabalhador, 11.5%, valor em %, decimal.Decimal
TAXA_IRS        -> Retenção aplicada ao trabalhador, 25%, valor em %, decimal.Decimal
CONT_SINDICATO  -> contribuição para o sindicato, 0.5%, valor em %, decimal.Decimal

SAÍDAS:
montante_ss     -> Montante para a seg. social, decimal.Decimal
                   montante_ss = salario_bruto * (TAXA_SS/100)
                   Este montante e os restantes são exibidos em STDOUT com 
                   2 casas decimais.
montante_irs    -> Desconto em sede de IRS, decimal.Decimal
                   montante_irs = salario_bruto * (TAXA_IRS/100)
montante_sind   -> contribuição (montante) para o sindicato, decimal.Decimal
                   montante_sind = salario_bruto * (CONT_SINDICATO/100)
salario_liquido -> salario_bruto menos os descontos, decimal.Decimal
                   salario_liquido = salario_bruto - montante_ss/irs/sind
                   
DESENHO: Não necessário
"""

from decimal import Decimal as dec

TAXA_SS  = dec('11.5')       # em %
TAXA_IRS = dec('25.0')       # em %
CONT_SINDICATO = dec('0.5')  # em % 

salario_bruto = dec(input("Salário bruto: "))
montante_ss = salario_bruto * (TAXA_SS/100)
montante_irs = salario_bruto * (TAXA_IRS/100)
montante_sind = salario_bruto * (CONT_SINDICATO/100)
salario_liquido = salario_bruto - montante_ss - montante_irs - montante_sind

print(f"Contribuição SS     : {montante_ss:7.2f}")
print(f"Montante IRS        : {montante_irs:7.2f}")
print(f"Montante sindicato  : {montante_sind:7.2f}")
print(f"Salário liquído     : {salario_liquido:7.2f}")
