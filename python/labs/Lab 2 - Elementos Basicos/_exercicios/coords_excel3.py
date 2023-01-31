"""
Programa para traduzir as coordenadas "simbólicas" do Excel 
para coordenadas lineares. Por exemplo, em Excel, internamente, 
a célula A1 corresponde à célula na linha 0 e coluna 0.
"""

def traduz_col(col: str) -> int:
    soma = 0
    exp = len(col) - 1
    for letra in col.upper():
        num = ord(letra) - ord('A') + 1
        soma += num * (26 ** exp)
        exp -= 1
    return soma - 1

coords = input("Indique as coordenadas: ")
while coords != 'sair':
    c, l = coords.split()
    print(f"Linha: {int(l)-1} Coluna: {traduz_col(c)}")
    print("--")
    coords = input("Indique as coordenadas: ")

print("Fim do programa")

