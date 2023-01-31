"""
SÉRIE DE EXERCÍCIOS 2

Calcula tempo em segundos após introdução de horas, minutos e
segundos.

DADOS DE ENTRADA:
    horas    : h, string -> int
    minutos  : m, string -> int
    segundos : s, string -> int

DADOS DE SAÍDA:
    segundos : total_segs, int
    total_segs = h*3600 + m*60 + s
"""
# pylint: disable=C0103

h = int(input("Horas    : "))
m = int(input("Minutos  : "))
s = int(input("Segundos : "))

print()
print("Total segundos: ", h*3600 + m*60 + s)
