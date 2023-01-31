"""
LABORATÓRIO 4

Exemplos, e respectiva teoria, a respeito de alguns dos conceitos 
que estão na base da Programação Orientada por Objectos (POO).
"""

import math
from enum import Enum


# ATENÇÃO: Desactivamos os seguintes avisos/erros devido apenas 
# ao tipo de documento que estamos a desenvolver. Na verdade, este
# ficheiro é mais um documento téorico sobre abstração e tópicos
# relacionados, do que um módulo de código em Python.
# Em código "normal" devemos deixar esses avisos/erros activos
# porque alertam para situações que são mesmo de evitar
#
# pylint: disable=W0621
# pylint: disable=E0102

"""
# EXEMPLO 2.1: OPERAÇÕES GENÉRICAS COM NÚMEROS COMPLEXOS - 
#              EXPEDIR/DESPACHAR POR TIPO (DISPATCH ON TYPE)

Com o exemplo anterior vimos que o princípio da abstracção de dados não
é, só por si, suficiente para que as duas representações de números 
complexos possam coexistir. Aliás, como ambas utilizam um tuplo para 
armazenar um par de valores, não temos como perceber a que se referem 
esses valores. Além do mais, as duas representações utilizam os mesmos
nomes para as operações elementares, o que leva que uma representação 
esconda a outra (este problema resolve-se facilmente colocando cada 
representação num módulo diferente, mas aqui vamos seguir uma abordagem 
diferente)

Para resolver o primeiro problema, perceber a que um objecto se refere, 
uma possível solução passa por anexar uma etiqueta ou rótulo com o tipo 
de representação, ou seja, assinar os objectos com a representação do 
número complexo. Uma forma eficiente de o fazer passa por definir uma 
enumeração de tipos de representação e depois devolver um par 
<TIPO, OBJECTO DE DADOS>.
"""

known_types = set()    # repositório ("registry") de tipos conhecidos


def attach_type(data_type, obj):
    known_types.add(data_type)
    return (data_type, obj)


def type_of(obj):
    if len(obj) != 2 and obj[0] not in known_types:
        raise TypeError('Object is not a valid typed object')
    return obj[0]


def contents_of(obj):
    if len(obj) != 2 and obj[0] not in known_types:
        raise TypeError('Object is not a valid typed object')
    return obj[1]

"""
Podemos olhar para ATTACH_TYPE como sendo um construtor que, dado um 
objecto qualquer, permite obter um objecto com tipo de representação,
ou seja, um objecto tipificado. TYPE_OF e CONTENTS_OF são os acessores
para este tipo de objectos.

Com estas funções, podemos desenvolver predicados para determinar se
um número complexo é rectangular ou polar. 
"""

ComplexType = Enum('ComplexType', 'RECTANGULAR POLAR')


def is_rectangular(z):
    return type_of(z) is ComplexType.RECTANGULAR


def is_polar(z):
    return type_of(z) is ComplexType.POLAR

"""
Os predicados em cima assinalam uma excepção se z não for um objecto
tipificado.

Temos que resolver ainda um problema para que as duas representações 
possam coexistir: o conflito de nomes iguais que existe entre as 
funções para uma notação e para outra. Uma forma de fazermos coexistir 
as duas representações passa por dar um sufixo correspondente a cada
função da representação rectangular e um sufixo diferente às funções
que tratam da outra forma. Por exemplo, as funções rectangulares 
passam a ser designadas de REAL_PART_RECT, IMAG_PART_RECT, etc., e
as polares ficam como REAL_PART_POLAR, IMAG_PART_POLAR, etc.
Depois desenvolvemos as funções REAL_PART, IMAG_PART, etc., que 
utilizam os predicados em cima definidos para agulharem para a função
apropriada, consoante a representação do complexo ser rectangular ou 
polar. 
"""

"""
Seguem-se as funções elementares para a representação rectangular:
"""

def complex_from_real_imag_rectang(r, i):
    contents = (r, i)
    return attach_type(ComplexType.RECTANGULAR, contents)


def complex_from_mag_angle_rectang(m, a):
    return complex_from_real_imag_rectang(m * math.cos(a), m * math.sin(a))


def real_part_rectang(z):
    return z[0]


def imag_part_rectang(z):
    return z[1]

def magnitude_rectang(z):
    return math.sqrt(real_part_rectang(z)**2 + imag_part_rectang(z) ** 2)


def angle_rectang(z):
    return math.atan2(imag_part_rectang(z), real_part_rectang(z))

"""
E agora seguem-se as funções elementares para a representação polar:
"""

def complex_from_real_imag_polar(r, i):
    return complex_from_mag_angle_polar(math.sqrt(r**2 + i**2), math.atan2(i, r))


def complex_from_mag_angle_polar(m, a):
    contents = m, a
    return attach_type(ComplexType.POLAR, contents)


def real_part_polar(z):
    return magnitude_polar(z) * math.cos(angle_polar(z))


def imag_part_polar(z):
    return magnitude_polar(z) * math.sin(angle_polar(z))


def magnitude_polar(z):
    return z[0]


def angle_polar(z):
    return z[1]

"""
E agora seguem-se as funções elementares para o conjunto de números 
complexos, seja qual for a representação. Ou seja, à excepção dos 
construtores, estas funções vão ser genéricas porque vão aceitar 
números complexos em ambas as representações. Vamos começar pelos 
acessores.
"""

def real_part(z):
    if is_rectangular(z):
        r = real_part_rectang(contents_of(z))
    elif is_polar(z):
        r = real_part_polar(contents_of(z))
    else:
        raise TypeError('Operation not defined for this type of object')
    return r


def imag_part(z):
    if is_rectangular(z):
        i = imag_part_rectang(contents_of(z))
    elif is_polar(z):
        i = imag_part_polar(contents_of(z))
    else:
        raise TypeError('Operation not defined for this type of object')
    return i


def magnitude(z):
    if is_rectangular(z):
        m = magnitude_rectang(contents_of(z))
    elif is_polar(z):
        m = magnitude_polar(contents_of(z))
    else:
        raise TypeError('Operation not defined for this type of object')
    return m


def angle(z):
    if is_rectangular(z):
        a = angle_rectang(contents_of(z))
    elif is_polar(z):
        a = angle_polar(contents_of(z))
    else:
        raise TypeError('Operation not defined for this type of object')
    return a

"""
Note-se que, em Python, poderíamos ter definido os módulos RECTANG
e POLAR, e ter definido REAL_PART_RECTANG/POLAR, IMAG_PART_RECTANG/
POLAR, etc., no módulo respectivo. Optámos por não fazer para manter
a explicação o mais geral possível e para que seja mais clara a 
necessidades de mecanismos como módulos e classes.

E agora os construtores. Faz sentido, quando se pretende obter
um número complexo através das suas partes real e imaginária, que esse
número seja construido na forma rectangular. Tal como faz sentido que 
se obtenha um número polar, quando se passa uma magnitude e um ângulo.
"""

def complex_from_real_imag(r, i):
    return complex_from_real_imag_rectang(r, i)


def complex_from_mag_angle(m, a):
    return complex_from_mag_angle_polar(m, a)

"""
As operações aritméticas com complexos, essas continuam a ser as mesmas:
"""

def add_complex(z1, z2):
    return complex_from_real_imag(
        real_part(z1) + real_part(z2),
        imag_part(z1) + imag_part(z2)
    )


def sub_complex(z1, z2):
    return complex_from_real_imag(
        real_part(z1) - real_part(z2),
        imag_part(z1) - imag_part(z2)
    )


def mul_complex(z1, z2):
    return complex_from_mag_angle(
        magnitude(z1) * magnitude(z2),
        angle(z1) + angle(z2)
    )


def div_complex(z1, z2):
    return complex_from_mag_angle(
        magnitude(z1) / magnitude(z2),
        angle(z1) - angle(z2)
    )


def pow_complex(z1, n: float):
    return complex_from_mag_angle(magnitude(z1) ** n, n * angle(z1))


def complex_to_str(z):
    r, i = real_part(z), imag_part(z)
    sign = '+' if i > 0 else ''
    dec_part_r, dec_part_i = r % 1, i % 1
    # round to int if the decimal part of the number is either too small 
    # or too large
    if dec_part_r < 0.0000001 or dec_part_r > 0.9999999: 
        r = round(r)          
    if dec_part_i < 0.0000001 or dec_part_i > 0.9999999: 
        i = round(i)          
    return f'{r}{sign}{i}i'

"""
A esta estratégia de verificar qual o tipo de dados de um objecto e de 
invocar a função ou método apropriado é designada de Expedir/Despachar
por Tipo (Dispatch on Type). Este estratégia permite obter modularidade.
Porém, a forma como a implementámos, apresenta alguns problemas. Para
já, não é facilmente extensível. Dado que todas as operações 
genéricas têm que conhecer todas as representações em concreto, se
pretendermos adicionar uma nova representação então temos que alterar
todas as funções elementares. Este exemplo é particularmente limitado,
mas o sistema seria muito difícil de manter caso existissem dezenas
de representações, e caso o número operações fosse muito maior.

# EXEMPLO 2.2: OPERAÇÕES GENÉRICAS COM NÚMEROS COMPLEXOS - 
#              PROGRAMAÇÃO ORIENTADA PELOS DADOS

Precisamos de uma forma de modularizar ainda mais o nosso sistema.
Olhando para a invocação de uma operação genérica, verificamos que, na
prática, é que como se fosse consultada uma tabela bidimensional que
contém as operações genéricas numa dimensão e os tipos de dados na 
outra dimensão. As entradas na tabela são as operações concretas. 
A Programação Orientada pelos Dados (Data-Directed Programming) 
consiste na técnica que utiliza uma tabela destas explicitamente para
localizar a implementação concreta da operação genérica.

                │  RECTANGULAR     │  POLAR
   ─────────────┼──────────────────┼─────────────
     REAL_PART  │  REAL_PART_RECT  │  REAL_PART_POLAR
     IMAG_PART  │  IMAG_PART_RECT  │  IMAG_PART_POLAR
     MAGNITUDE  │  MAGNITUDE_RECT  │  MAGNITUDE_POLAR
     ANGLE      │  ANGLE_RECT      │  ANGLE_POLAR

Na verdade, como veremos, as entradas nesta tabela nem necessitam de 
ser funções com os nomes com sufixos _RECTANG ou _POLAR. Nem sequer
necessitam de nomes.

Assumindo que esta tabela existe, podemos aceder através das duas 
funções seguintes:
- PUT_OPERATION(<TABLE>, <OP>, <TYPE>, <ITEM>): coloca o <ITEM> na 
  célula situada na linha <OP> e coluna <TYPE>.
- GET_OPERATION(<TABLE>, <OP>, <TYPE>): obtém o <ITEM> na célula situada ...

Existem muitas formas de representar esta tabela. Neste exemplo, vamos 
recorrer a um dicionário, indexado por um tuplo (OPERAÇÃO, TIPO).
Como seria de esperar, utilizamos abstração de dados para implementar
esta tabela, escondendo a sua representação em concreto atrás de um 
construtor e de vários acessores e modificadores.
"""

def make_dispatch_table():
    return set(), set(), {}  # operation names, types, table values


def dispatch_operation_names(table) -> set:
    return table[0]


def dispatch_types(table) -> set:
    return table[1]


def dispatch_operations(table) -> dict:
    return table[2]

"""
E agora as operações principais para manipulação da tabela de expedição, 
aquelas que devem ser utilizadas pelas representações de números 
complexos para adicionarem as respectivas operações ao sistema.
"""

def put_operation(table, operation_name, type_, operation):
    dispatch_operation_names(table).add(operation_name)
    dispatch_types(table).add(type_)
    dispatch_operations(table)[operation_name, type_] = operation


def get_operation(table, operation_name, type_):
    if operation_name not in dispatch_operation_names(table):
        raise TypeError(f'Invalid operation {operation_name}')
    if type_ not in dispatch_types(table):
        raise TypeError(f'Invalid type {type_}')
    return dispatch_operations(table)[operation_name, type_]


def operate1(table, operation, obj):
    func = get_operation(table, operation, type_of(obj))
    if not func:
        raise TypeError(f'No valid operation for {operation} '
                        'on operand type {type_of(obj)}')
    return func(contents_of(obj))


dispatch_table = make_dispatch_table()


ComplexOperation = Enum('ComplexOperation', (
    'REAL_PART', 
    'IMAG_PART', 
    'MAGNITUDE', 
    'ANGLE',
    'COMPLEX_FROM_REAL_IMAG',
    'COMPLEX_FROM_MAG_ANGLE',
))


def install_rectangular():
    Type, Oper = ComplexType, ComplexOperation

    def complex_from_real_imag(r, i):
        # print('install_rectangular COMPLEX_FROM_REAL_IMAG')
        contents = (r, i)
        return attach_type(ComplexType.RECTANGULAR, contents)

    def complex_from_mag_angle(m, a):
        # print('install_rectangular COMPLEX_FROM_MAG_ANGLE')
        contents = (m * math.cos(a), m * math.sin(a))
        return attach_type(ComplexType.RECTANGULAR, contents)

    def real_part(z):
        return z[0]

    def imag_part(z):
        return z[1]

    def magnitude(z):
        return math.sqrt(real_part(z)**2 + imag_part(z) ** 2)

    def angle(z):
        return math.atan2(imag_part(z), real_part(z))

    put_operation(dispatch_table, Oper.COMPLEX_FROM_REAL_IMAG, Type.RECTANGULAR, 
                  complex_from_real_imag)
    put_operation(dispatch_table, Oper.COMPLEX_FROM_MAG_ANGLE, 
                  Type.RECTANGULAR, complex_from_mag_angle)
    put_operation(dispatch_table, Oper.REAL_PART, Type.RECTANGULAR, real_part)
    put_operation(dispatch_table, Oper.IMAG_PART, Type.RECTANGULAR, imag_part)
    put_operation(dispatch_table, Oper.MAGNITUDE, Type.RECTANGULAR, magnitude)
    put_operation(dispatch_table, Oper.ANGLE, Type.RECTANGULAR, angle)


def install_polar():
    Type, Oper = ComplexType, ComplexOperation

    def complex_from_real_imag(r, i):
        # print('install_polar COMPLEX_FROM_REAL_IMAG')
        contents = (math.sqrt(r**2 + i**2), math.atan2(i, r))
        return attach_type(ComplexType.POLAR, contents)

    def complex_from_mag_angle(m, a):
        # print('install_polar COMPLEX_FROM_MAG_ANGLE')
        contents = (m, a)
        return attach_type(ComplexType.POLAR, contents)

    def real_part(z):
        return magnitude(z) * math.cos(angle(z))

    def imag_part(z):
        return magnitude(z) * math.sin(angle(z))

    def magnitude(z):
        return z[0]

    def angle(z):
        return z[1]

    put_operation(dispatch_table, Oper.COMPLEX_FROM_REAL_IMAG, Type.POLAR, 
                  complex_from_real_imag)
    put_operation(dispatch_table, Oper.COMPLEX_FROM_MAG_ANGLE, Type.POLAR, 
                  complex_from_mag_angle)
    put_operation(dispatch_table, Oper.REAL_PART, Type.POLAR, real_part)
    put_operation(dispatch_table, Oper.IMAG_PART, Type.POLAR, imag_part)
    put_operation(dispatch_table, Oper.MAGNITUDE, Type.POLAR, magnitude)
    put_operation(dispatch_table, Oper.ANGLE, Type.POLAR, angle)


def complex_from_real_imag(r, i):
    operation, type_ = ComplexOperation.COMPLEX_FROM_REAL_IMAG, ComplexType.RECTANGULAR
    constructor = get_operation(dispatch_table, operation, type_)
    return constructor(r, i)


def complex_from_mag_angle(m, a):
    operation, type_ = ComplexOperation.COMPLEX_FROM_MAG_ANGLE, ComplexType.POLAR
    constructor = get_operation(dispatch_table, operation, type_)
    return constructor(m, a)


def real_part(z):
    return operate1(dispatch_table, ComplexOperation.REAL_PART, z)


def imag_part(z):
    return operate1(dispatch_table, ComplexOperation.IMAG_PART, z)


def magnitude(z):
    return operate1(dispatch_table, ComplexOperation.MAGNITUDE, z)


def angle(z):
    return operate1(dispatch_table, ComplexOperation.ANGLE, z)

"""
# EXEMPLO 2.3: OPERAÇÕES GENÉRICAS COM NÚMEROS - 

No exemplo anterior, vimos como conceber sistemas que suportam múltiplas
representações para um objecto de dados. As técnicas vistas permitem
estabelecer uma ligação entre o código que implementa as operações (*)
e as diferentes representações por meio de operações genéricas (**).

(*)  -> No exemplo anterior, ADD_COMPLEX, SUB_COMPLEX, etc.
(**) -> No exemplo anterior, REAL_PART, IMAG_PART, etc.

Neste exemplo vamos levar esta ideia ainda mais longe e, além de 
definirmos operações que são genéricas perante diferentes representações
representações, vamos também definir operações que são genéricas perante
diferentes tipos de objectos de dados. Neste exemplo vamos unificar as
operações aritméticas para os diversos tipos de números com que temos 
lidado: números complexos, números racionais, e os números "nativos" de 
Python: int e float.

  ───────────────────────────────────────────────────────────────────────────────────
            ADD         SUB         MUL         DIV         POW    ...
  ─────────────────────────┬──────────────────────────────┬──────────────────────────
    ADD_RAT, SUB_RAT,      │  ADD_COMPLEX, SUB_COMPLEX,   │  +, -, *, /, ...
    MUL_RAT, ...           │  MUL_COMPLEX, ...            │
                           │                              │                           
    Aritmética c/ números  │  Arimética c/ números        │  Aritmética c/ números
    números racionais      │  complexos                   │  "nativos" 
                           ├──────────────┬───────────────┤
                           │              │               │
                           │  RECTANGULAR │     POLAR     │
                           │              │               │
  ─────────────────────────┴──────────────┴───────────────┴─────────────────────────
"""

AritmOperation = Enum('AritmOperation', (
    'ADD',
    'SUB',
    'MUL',
    'DIV',
    'POW',
    # 'COMPLEX_FROM_REAL_IMAG',    # construtor para num complexo
    # 'COMPLEX_FROM_MAG_ANGLE',    # construtor para num complexo
    # 'RATIONAL',                  # construtor para num racional
))


NumberType = Enum('NumberType', (
    'COMPLEX',
    'RATIONAL',
    'PYTHON_NUMBER',    # int, float
))


def operate2(table, operation, obj1, obj2):
    func = get_operation(table, operation, (type_of(obj1), type_of(obj2)))
    if not func:
        raise TypeError(f'No valid operation for {operation} on '
                        'operand types {type_of(obj1)}, {type_of(obj2)}.')
    return func(contents_of(obj1), contents_of(obj2))


def add(x, y):
    return operate2(dispatch_table, AritmOperation.ADD, x, y)


def sub(x, y):
    return operate2(dispatch_table, AritmOperation.SUB, x, y)


def mul(x, y):
    return operate2(dispatch_table, AritmOperation.MUL, x, y)


def div(x, y):
    return operate2(dispatch_table, AritmOperation.DIV, x, y)


def pow_(b, e):
    return operate2(dispatch_table, AritmOperation.POW, b, e)


# OPERATE2 suporta dois argumentos (o que faz sentido para a maioria das 
# operações aritméticas que se escrevem na forma infixa e, como tal, têm 
# 2 operandos). Em seguida mostra-se uma versão de OPERATE que permite 
# implementar operações aritméticas para N operandos.

# def operateN(operation, *objs):
#     func = get_operation(dispatch_table, operation, tuple(type_of(obj) for obj in objs))
#     if not func:
#         raise TypeError(f'No valid operation for {operation} on '
#                         'operand types {[type_of(obj) for obj in objs]}')
#     return func(*(contents_of(obj) for obj in objs))


# def add(x, y):
#     return operateN(Operation.ADD, x, y)


# def sub(x, y):
#     return operateN(Operation.SUB, x, y)


# def mul(x, y):
#     return operateN(Operation.MUL, x, y)


# def div(x, y):
#     return operateN(Operation.DIV, x, y)

# Dentro do mesmo espírito, poderíamos definir um construtor genérico 
# como, por exemplo, o seguinte:
#
# def make(type_: NumberType, *objs):
#     obj_types = (type_of(obj) for obj in objs)
#     constructor = get_operation(dispatch_table, type_, tuple(obj_types))
#     return constructor(*objs)


def install_python_number():
    Oper, suported_types = AritmOperation, (NumberType.PYTHON_NUMBER, NumberType.PYTHON_NUMBER)

    def add(x, y):
        return python_number(x + y)

    def sub(x, y):
        return python_number(x - y)
        
    def mul(x, y):
        return python_number(x * y)
        
    def div(x, y):
        return python_number(x / y)
        
    def pow_(b, e):
        return python_number(b ** e)
        
    def python_number(x):
        return attach_type(NumberType.PYTHON_NUMBER, x)

    put_operation(dispatch_table, Oper.ADD, suported_types, add)
    put_operation(dispatch_table, Oper.SUB, suported_types, sub)
    put_operation(dispatch_table, Oper.MUL, suported_types, mul)
    put_operation(dispatch_table, Oper.DIV, suported_types, div)
    put_operation(dispatch_table, Oper.POW, suported_types, pow_)
    put_operation(dispatch_table, NumberType.PYTHON_NUMBER, NumberType.PYTHON_NUMBER, 
                  python_number)


def python_number(x): 
    operation, type_ = NumberType.PYTHON_NUMBER, NumberType.PYTHON_NUMBER
    constructor = get_operation(dispatch_table, operation, type_)
    return constructor(x)


def install_rational():
    Oper, suported_types = AritmOperation, (NumberType.RATIONAL, NumberType.RATIONAL)

    def add(x, y):
        return rat(numer(x)*denom(y) + numer(y)*denom(x), denom(x) * denom(y))

    def sub(x, y):
        return rat(numer(x)*denom(y) - numer(y)*denom(x), denom(x) * denom(y))

    def mul(x, y):
        return rat(numer(x) * numer(y), denom(x) * denom(y))

    def div(x, y):
        return rat(numer(x) * denom(y), denom(x) * numer(y))

    def pow_(b, e):
        return rat(numer(b) ** e, denom(b) ** e)

    def rat(n: int, d: int):
        g = math.gcd(n, d)
        return attach_type(NumberType.RATIONAL, (n//g, d//g))

    def numer(x):
        return x[0]

    def denom(x):
        return x[1]

    put_operation(dispatch_table, Oper.ADD, suported_types, add)
    put_operation(dispatch_table, Oper.SUB, suported_types, sub)
    put_operation(dispatch_table, Oper.MUL, suported_types, mul)
    put_operation(dispatch_table, Oper.DIV, suported_types, div)
    put_operation(dispatch_table, Oper.POW, suported_types, pow_)
    put_operation(dispatch_table, NumberType.RATIONAL, (int, int), rat)


def rational(n: int, d: int):
    operation, types = NumberType.RATIONAL, (int, int)
    constructor = get_operation(dispatch_table, operation, types)
    return constructor(n, d)


def install_complex():
    Oper, suported_types = AritmOperation, (NumberType.COMPLEX, NumberType.COMPLEX)

    def add(z1, z2):
        return complex_from_real_imag(
            real_part(z1) + real_part(z2),
            imag_part(z1) + imag_part(z2)
        )

    def sub(z1, z2):
        return complex_from_real_imag(
            real_part(z1) - real_part(z2),
            imag_part(z1) - imag_part(z2)
        )

    def mul(z1, z2):
        return complex_from_mag_angle(
            magnitude(z1) * magnitude(z2),
            angle(z1) + angle(z2)
        )

    def div(z1, z2):
        return complex_from_mag_angle(
            magnitude(z1) / magnitude(z2),
            angle(z1) - angle(z2)
        )

    def pow_(z1, n: float):
        return complex_from_mag_angle(magnitude(z1) ** n, n * angle(z1))

    def complex_from_real_imag(r, i):
        operation, type_ = ComplexOperation.COMPLEX_FROM_REAL_IMAG, ComplexType.RECTANGULAR
        constructor = get_operation(dispatch_table, operation, type_)
        return attach_type(NumberType.COMPLEX, constructor(r, i))

    def complex_from_mag_angle(m, a):
        operation, type_ = ComplexOperation.COMPLEX_FROM_MAG_ANGLE, ComplexType.POLAR
        constructor = get_operation(dispatch_table, operation, type_)
        return attach_type(NumberType.COMPLEX, constructor(m, a))

    put_operation(dispatch_table, Oper.ADD, suported_types, add)
    put_operation(dispatch_table, Oper.SUB, suported_types, sub)
    put_operation(dispatch_table, Oper.MUL, suported_types, mul)
    put_operation(dispatch_table, Oper.DIV, suported_types, div)
    put_operation(dispatch_table, Oper.POW, suported_types, pow_)
    put_operation(dispatch_table, NumberType.COMPLEX, 
                  (ComplexType.RECTANGULAR, float, float), complex_from_real_imag)
    put_operation(dispatch_table, NumberType.COMPLEX, 
                  (ComplexType.POLAR, float, float), complex_from_mag_angle)


def complex_from_real_imag(r, i):
    operation, type_ = NumberType.COMPLEX, (ComplexType.RECTANGULAR, float, float)
    constructor = get_operation(dispatch_table, operation, type_)
    return constructor(r, i)


def complex_from_mag_angle(m, a):
    operation, type_ = NumberType.COMPLEX, (ComplexType.POLAR, float, float)
    constructor = get_operation(dispatch_table, operation, type_)
    return constructor(m, a)
