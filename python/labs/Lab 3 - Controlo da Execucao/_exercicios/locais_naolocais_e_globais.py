"""
SÉRIE DE EXERCÍCIOS 3 - Controlo da Execução

O que é exibido pelo seguinte código (divido em três partes).
"""

y = 10
def f(x):
    print(x + y)
f(3)
def g():
    y = 20
    f(3)
g()

print('#####')

y = 5
def func1():
    def f(x):
        print(x + y)
    f(10)
def func2():
    def f(x):
        print(x + y)
    y = 50
    f(10)
func1()
func2()

print('#####')

y = 10
def func3():
    def f1():
        y = 1
    def f2():
        nonlocal y
        y = 2
    def f3():
        global y
        y = 3
    y = 0
    f1()
    print(y)
    f2()
    print(y)
    f3()
    print(y)
func3()
print(y)


