
nome = 'ALBERTO'
nums = (10, 21, 3, 87, -10, 18, 17, 301, -450, 28, 8, 5, 4)
pessoas = {'ana': 23, 'bruno': 40, 'carlos': 15}

for x in nome:
    print(x)

for x in nums:
    print(x)

for x in pessoas:
    print(x)

# def mapeia(itens, fun):
#     itens2 = []
#     for item in itens:
#         itens2.append(fun(item))
#     return itens2

# def filtra(itens, criterio):
#     seleccionados = []
#     for item in itens:
#         if criterio(item):
#             seleccionados.append(item)
#     return seleccionados    

def mapeia(itens, fun):
    for item in itens:
        yield fun(item)

def filtra(itens, criterio):
    for item in itens:
        if criterio(item):
            yield item


nums = (10, 21, 3, 87, -10, 18, 17, 301, -450, 28, 8, 5, 4)
#...
nums3 = mapeia(nums, lambda x: x * 3)
#...
pares = filtra(nums3, lambda x: x % 2 == 0)
#...
pares_positivos = filtra(pares, lambda x: x > 0)
#...
pares_positivos_entre_0_e_100 = filtra(pares_positivos, lambda x: 0 < x < 100)


# EXPRESSÃO GERADORA:
#   (EXPRESSÃO(VAR) for VAR in ITERÁVEL)
#   (EXPRESSÃO(VAR) for VAR in ITERÁVEL if CRITERIO(VAR))


>>> list(date_range(date(2020, 1, 15), date(2020, 1, 20)))
[
    date(2020, 1, 15),
    date(2020, 1, 16),
    date(2020, 1, 17),
    date(2020, 1, 18),
    date(2020, 1, 19)
]

>>> it = date_range(date(2020, 2, 28), date(2020, 3, 1))
>>> next(it)
date(2020, 2, 28)
>>> next(it)
date(2020, 2, 29)
>>> next(it)
StopIteration

>>> list(date_range(date(2020, 3, 1), date(2020, 2, 28)))
[]
>>>  list(date_range(date(2020, 3, 1), date(2020, 2, 28), -1))
[date(2020, 3, 1), date(2020, 2, 29)]

>>> list(date_range(date(2020, 2, 28), date(2020, 3, 5), 2))
[date(2020, 2, 28), date(2020, 3, 1), date(2020, 3, 3)]
