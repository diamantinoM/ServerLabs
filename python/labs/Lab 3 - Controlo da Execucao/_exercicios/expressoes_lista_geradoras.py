"""
SÉRIE DE EXERCÍCIOS 3 - Controlo da Execução

Complemento à resolução de alguns dos exercícios de revisão do 
Laboratório 3 - Extra
"""

nums = (10, 1, 2, 7, 3, 13, 18, 1, 12)


def obtemPares(seq):
    pares = []
    for num in seq:
        if num % 2 == 0:
            pares.append(num)
    return pares


def iteraPares(seq):
    for num in seq:
        if num % 2 == 0:
            yield num

# .__next__ (permite invocar next(gerador))
# .__iter__ (permite invocar iter(gerador))
# .send     (permite invocar gerador.send())
# .close    (permite invocar gerador.close())

def obtemPares2(seq):
    return [num for num in seq if num % 2 == 0]

def iteraPares2(seq):
    return (num for num in seq if num % 2 == 0)


##
## 1a Linha

nums = [19, 35, 9, 10, 20, 17, 12, 22, 10]

# Ciclo a produzir uma lista
maiores_que_15 = []
for num in nums:
    if num >= 15:
        maiores_que_15.append(num)

# Gerador a devolver cada elemento com yield
def filtra_maiores_que_15(seq):
    for num in seq:
        if num >= 15:
            yield num

list(filtra_maiores_que_15(nums))

# Expressão lista/geradora
[x for x in nums if x >= 15]

##
## 2a Linha

txt = 'ALBERTO'

# Ciclo a produzir uma lista
txt2 = []
for i in range(len(txt)-1, -1, -1):
    txt2.append(txt[i])
txt2 = ''.join(txt2)

# Gerador a devolver cada elemento com yield
def inverte(txt):
    for i in range(len(txt)-1, -1, -1):
        yield txt[i]

''.join(inverte(txt))

# ineficiente mas correcto e legível
# txt2 = ''
# for ch in txt:
#     txt2 = ch + txt2

# Expressão lista/geradora
''.join(txt[i] for i in range(len(txt)-1, -1, -1))

## 
## 3a Linha

texto = 'Bom dia. Hoje temos aulas.'

# Duas soluções com ciclos:
# 1a
vogais = {'a': False, 'e': False, 'i': False, 'o': False, 'u': False}

for ch in texto:
    if ch in 'aeiou':
        vogais[ch] = True

sum(vogais.values()) == 5

# 2a
contador = 0
for ch in set(texto):
    if ch in 'aeiou':
        contador += 1
contador == 5

# Duas soluções sem ciclos
len(set(texto) & {'a', 'e', 'i', 'o', 'u'}) == 5

# Expressão lista/geradora
len(set(ch for ch in texto if ch in 'aeiou')) == 5