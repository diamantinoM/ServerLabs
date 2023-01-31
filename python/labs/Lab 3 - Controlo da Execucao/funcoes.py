##########################################
#
#       FUNÇÕES
#
##########################################

from decimal import Decimal as dec

# concat('abc', 'def')  => 'abcdef'
# concat('abc', 23, dec('23.2'), True)  => 'abc2323.2True'
# concat('abc', -1, [2.5, 90])  => 'abc-1[2.5, 90]'
# concat('abc', -1, [2.5, 90], '++')      => 'abc-1[2.5, 90]++'
# concat('abc', -1, [2.5, 90], sep='++')  => 'abc++-1++[2.5, 90]'

def concat(*args, sep='', end=''):
    items_str = []
    for arg in args:
        items_str.append(str(arg))
    return sep.join(items_str) + end

# def soma(a: int, b: int) -> int:
#     return a + b

# def repete(txt: str, a: int) -> str:
#     return a * txt


# print(soma(2, 3))
# print(soma("alberto", "armando"))

# print(repete("alberto", 4))

# print(repete(a=4, txt="alberto"))

def fun1(a, b, *args):
    print(a)
    print(b)
    print(args)

fun1(1, 2, 3, 4, 5)

def fun2(a, b, *args, c):   # sim, isto é possível...
    print(a)
    print(b)
    print(args)
    print(c)

def fun3(a, b, *args, c=78, d=90, **kargs):
    print(a)
    print(b)
    print(args)
    print(c)
    print(d)
    print(kargs)

    def fun4(*args, **kargs):
        print(args)
        print(kargs)

#####################################################
# 
#       FUNÇÕES DE PRIMEIRA ORDEM
#       Funções parametrizadas com outras funções
#
#####################################################

nums = [100, -2, -1, 59, 44, 46, 77]    
nomes = ['alberto', 'bruno', 'armando', 'josé', 'albertina']

def filtra_positivos(itens):
    seleccionados = []
    for item in itens:
        if item > 0:
            seleccionados.append(item)
    return seleccionados

def filtra_pares(itens):
    seleccionados = []
    for item in itens:
        if item % 2 == 0:
            seleccionados.append(item)
    return seleccionados

def filtra_maiores_que_50(itens):
    seleccionados = []
    for item in itens:
        if item >= 50:
            seleccionados.append(item)
    return seleccionados

def filtra_tamanho_menor_que_6(itens):
    seleccionados = []
    for item in itens:
        if len(item) < 6:
            seleccionados.append(item)
    return seleccionados    

def filtra(itens, criterio):
    seleccionados = []
    for item in itens:
        if criterio(item):
            seleccionados.append(item)
    return seleccionados    


def e_positivo(num):
    return num > 0

def e_par(num):
    return num % 2 == 0

def e_par_positivo(num):
    return num % 2 == 0 and num > 0

def e_maior_que_50(num):
    return num >= 50

def tamanho_menor_que_6(txt):
    return len(txt) < 6

filtra(nums, e_positivo)
filtra(filtra(nums, e_positivo), e_par)
filtra(nums, e_maior_que_50)
filtra(nomes, tamanho_menor_que_6)

# LAMBDAS: Funções anónimas, com return implícito; são expressões

filtra(nums, lambda x: x > 0)
filtra(nums, lambda x: x % 2 == 0)
filtra(nums, lambda x: x % 2 == 0 and x > 0)
filtra(nums, lambda x: x > 50)
filtra(nomes, lambda txt: len(txt) < 6)
filtra(nomes, lambda nome: nome[0] in 'aeiouAEIOU')


letra = input("Letra: ")
filtra(nomes, lambda nome: nome[0] == letra)

# MAPEIA

def mapeia(itens: Iterable, mapeamento) -> list:
    transformados = []
    for item in itens:
        transformados.append(mapeamento(item))
    return transformados

def primeiro_car(string):
    return string[0]

def dobro(num):
    return 2 * num

mapeia(nomes, primeiro_car)
mapeia(numeros, dobro)

mapeia(nomes, lambda nome: nome[0])
mapeia(numeros, lambda numero: 2 * numero)

mapeia(numeros, lambda x: 2 * x)      # [-10, 0, 200, -4, -2, 118, 88, 92, 154]
mapeia(numeros, lambda x: x + 1)      # [-4, 1, 101, -1, 0, 60, 45, 47, 78]
mapeia(nomes, lambda nome: nome[-1])  # ['o', 'o', 'o', 'é', 'a']
mapeia(nomes, len)                    # [7, 5, 7, 4, 9]

# FILTER, MAP

nums = [100, -2, -1, 59, 44, 46, 77]    
nomes = ['alberto', 'bruno', 'armando', 'josé', 'albertina']

filter(lambda x: x > 0, nums)
map(lambda x: 2 * x, nums)

# EXPRESSÃO LISTA:
#   [EXPRESSÃO(VAR) for VAR in ITERÁVEL]
#   [EXPRESSÃO(VAR) for VAR in ITERÁVEL if CRITERIO(VAR)]

print([num for num in nums if num > 0])
print([2 * num for num in nums])

#####################################################
# 
#       FUNÇÕES INTERNAS / ANINHADAS / NESTED
#       RECURSIVIDADE
#
#####################################################

def e_palindromo(txt):
    """
    Detecta se a string `txt` é um palíndromo. Ignora a capitalização
    das letras e todos os caracteres que não sejam letras ou números.
    """
    def e_pal(seq_chs):
        if len(seq_chs) <= 1:
            return True
        return seq_chs[0] == seq_chs[-1] and e_pal(seq_chs[1:-1])

    return e_pal([ch for ch in txt.lower() if ch.isalnum()])


# factorial e analisar

def fibI(n):
    if n in (0, 1):
        return n
    x, y = 0, 1
    for _ in range(2, n+1):
        y, x = y + x, y
    return y

def fibR(n):
    if n in (0, 1):
        return n
    return fibR(n - 1) + fibR(n - 2)


# def find(itens, a):
#     for item in itens:
#         if item == a:
#             return True
#     return False

# def find(itens, a):
#     if not itens:
#         return False
#     elif itens[0] == a:
#         return True
#     return find(itens[1:], a)

# def inverte(lista):
#     return [] if len(lista)==0 else inverte(lista[1:]) + [lista[0]]

# def inverte1(lista):
#     return [] if len(lista)==0 else append_fn(inverte1(lista[1:]), lista[0])

# def append_fn(lista, item):
#     lista.append(item)
#     return lista

# def inverte2(lista):
#     return [] if not lista else list((*inverte2(lista[1:]), lista[0]))

# def inverte3(lista):
#     return [] if not lista else [*inverte3(lista[1:]), lista[0]]
    
#####################################################
# 
#       FUNÇÕES INTERNAS: CLOSURES
#
#####################################################

# def verde(Z):
#     X = ...    # definir X
#     def vermelha(...):
#         Y = ...
#         # tem acesso a X e a Y e a Z
#         ...
#     ...
#     # tem acesso apenas X 
#     return vermelha 
#
#         ┌─────────────────────────────────┐
#         │              ┌───────────────┐  │
#         │              │               │  │
#         │  VERMELHA    │     VERDE     │  │
#         │              │               │  │
#         │              └───────────────┘  │
#         └─────────────────────────────────┘

def somador(n):
    def soma(x):
        return n + x
    return soma    

soma10 = somador(10)
soma20 = somador(20)

print(soma10(3))  # 13
print(soma20(3))  # 23


def contador():
    i = 0
    def conta():
        nonlocal i
        i += 1
        return i
    return conta
         

months = [
    'January',
    'February',
    'March',
    'April',
    'May',
    'June',
    'July',
    'August',
    'September',
    'October',
    'November',
    'December'
]

def month_to_name(month_num: int):
    return months[month_num-1]

def month_to_name(month_num: int):
    months = [
        'January',
        'February',
        'March',
        'April',
        'May',
        'June',
        'July',
        'August',
        'September',
        'October',
        'November',
        'December'
    ]
    return months[month_num-1]

def make_month_to_name():
    months = [
        'January',
        'February',
        'March',
        'April',
        'May',
        'June',
        'July',
        'August',
        'September',
        'October',
        'November',
        'December'
    ]
    return lambda month_num: months[month_num-1]

month_to_name = make_month_to_name()
month_to_name(2)