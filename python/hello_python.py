import sys          # módulo com definições sobre o sistema

def greeting(name: str):
    print(f"Hello {name}")

print("Olá!")
greeting(sys.argv[1])
print("Adeus!")

# greeting(input("Como se chama? "))

# function greeting(name) {
#     console.log(`Hello ${name}`);
# } 

# sys.argv é uma lista (objecto do tipo list)
# Na 1a posição da lista aparece o nome do script ('hello_python.py'). Os 
# argumentos do script surgem a partir da 2a posição (inclusive).

# Uma lista é similar aos arrays do JavaScript

# JS     : let vals = [10, 20, 30];
# Python : vals = [10, 20, 30]

# import sys : lê o módulo sys para memória, e coloca o nome 'sys' no 
#  espaço de nomes deste script/módulo.
#  JS       : import * from 'sys'

# Uma lista (list) é uma sequência MUTÁVEL e heterogénea de valores
#       lista = [10, 20, 30]
#
# Um tuplo (tuple) é uma sequência IMUTÁVEL e heterogénea de valores
#       tuplo = (10, 20, 30)