"""
SÉRIE DE EXERCÍCIOS 3

Faça um programa que pergunta o nome do utilizador e caso seja um nome 
feminino, deverá dizer "Bom dia, Madame". No caso de ser um nome 
masculino, deverá então dizer "Bom dia, Cavalheiro". Numa primeira 
versão, utilize uma lista de nomes femininos e outra de nomes 
masculinos. Numa segunda versão utilize um dicionário de nomes com 
duas chaves: 'feminino', 'masculino'. Os valores de cada uma destas 
chaves são as listas da 1a versão.
 """

def cumprimenta_v1():
    femininos = ['Anabela', 'Armanda', 'Alberta', 'Angelina']
    masculinos = ['Alberto', 'Armando', 'António', 'Arnaldo']

    nome = input("Como se chama? ").capitalize()
    print(
        "Bom dia, Madame" if nome in femininos else
        "Bom dia, Cavalheiro" if nome in masculinos else
        "Bom dia"
    )


def cumprimenta_v2():
    nomes = {
        'femininos': ['Anabela', 'Armanda', 'Alberta', 'Angelina'],
        'masculinos': ['Alberto', 'Armando', 'António', 'Arnaldo']
    }

    nome = input("Como se chama? ").capitalize()
    print(
        "Bom dia, Madame" if nome in nomes['femininos'] else
        "Bom dia, Cavalheiro" if nome in nomes['masculinos'] else
        "Bom dia"
    )

