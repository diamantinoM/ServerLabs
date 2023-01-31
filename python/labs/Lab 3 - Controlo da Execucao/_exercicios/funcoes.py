"""
SÉRIE DE EXERCÍCIOS 3 - Controlo da Execução

Algumas das funções pedidas na série de exercícios 3.
"""

#######################################################################
## DOBRO, TRIPLO, QUADRADO e CUBO
#######################################################################

def dobro(a):
    return 2*a


def triplo(a):
    return 3*a


def quadrado(a):
    return a*a


def cubo(a):
    return a*a*a

#######################################################################
## RESOLVENTE
#######################################################################

import math

def resolvente(a, b, c):
    """
    Cálcula a fórmula resolvente. Devolve um tuplo com as duas raízes 
    da fórmula  para os coeficientes a, b e c. Se não tiver raízes,
    devolve None.
    """
    sqroot =  math.sqrt(b*b - 4*a*c) 
    return (-b + sqroot)/(2*a) , (-b -sqroot)/(2*a)

# testar: 
# resolvente(2, 3, 1)
# resolvente(2, -3, 1)
# resolvente(1, 3, 1)
# resolvente(4, 2, 1)
# resolvente(4, 2, -1)
# resolvente(4, 0, -16)

#######################################################################
## CONFIRMA
#######################################################################

def confirma(
    msg, 
    tentativas=4, 
    msg_erro="Introduza (S)im ou (N)ao",
):
    """
    Desenvolva a funcão confirma que solicita uma confirmação ao 
    utilizador. Enquanto o utilizador não introduzir 'sim', 's', 'não', 
    'nao' ou 'n', a função repete a mensagem de confirmação. Ao fim de um 
    número de tentativas (quatro, por omissão) a funçao desiste e assume 
    que o utilizador não confirmou. A função devolve True, se o 
    utilizador confirmar, e False, caso contrário. Além da mensagem de 
    confirmação e do número de tentativas, a função recebe uma mensagem
    de erro que deverá ser exibida quando o utilizador não introduzir o 
    pedido. Este parâmetro deve possuir o valor por omissão: 
      "Introduza (S)im ou (N)ao".
    """
    for i in range(tentativas):
        print()
        opcao = input(msg).strip().lower()
        if opcao in ('sim', 's'):
            return True
        elif opcao in ('não', 'nao', 'n', ''):
            return False
        else:
            print(msg_erro)
    return False

#######################################################################
## INVERTE
#######################################################################

def inverte(seq):
    """
    Desenvolva a função inverte que recebe uma sequência de elementos e 
    devolve uma lista com os elementos por ordem ordem inversa. 
    Não utilize `reversed` ou qualquer outra função já desenvolvida para 
    o efeito.    
    """
    val = []
    for i in range(len(seq)):
        val.append(seq[-(i + 1)])
    return val

#######################################################################
## INVERTE
#######################################################################

def invertePalavras1(str_):
    """
    Desenvolva a função `invertePalavras` que recebe uma string e
    devolve uma nova string com todas as palavras por ordem inversa. 
    Assuma que as palavras estão separadas apenas por um espaço.
    Esta versão não utiliza quaisquer funções/métodos para trabalhar
    com strings, como str.split, str.partition, etc.
    """
    # palavras = palavra = [] --> não funciona. porquê?
    palavras = []
    palavra = []
    for i, ch in enumerate(str_):
        if ch.isspace():
            if palavra:
                palavras.append(''.join(palavra))
                palavra = []
        else:
            palavra.append(ch)

    if palavra:
        # Se str_ não terminar num espaço, `palavra` ainda tem 
        # caracteres (ie, ainda tem uma palavra) que ainda não
        # foi adicionada à lista de palavras. 
        palavras.append(''.join(palavra))

    return ' '.join(reversed(palavras))  # será batota? se sim, ver versão em baixo


from collections import deque

def invertePalavras2(str_):
    """
    Desenvolva a função `invertePalavras` que recebe uma string e
    devolve uma nova string com todas as palavras por ordem inversa. 
    Assuma que as palavras estão separadas apenas por um espaço.
    Esta versão não utiliza quaisquer funções/métodos para trabalhar
    com strings, como str.split, str.partition, etc.
    """
    palavras = deque()
    palavra = []
    for i, ch in enumerate(str_):
        if ch.isspace():
            if palavra:
                palavras.appendleft(''.join(palavra))
                palavra = []
        else:
            palavra.append(ch)

    if palavra:
        # Se str_ não terminar num espaço, `palavra` ainda tem 
        # caracteres (ie, ainda tem uma palavra) que ainda não
        # foi adicionada à lista de palavras. 
        palavras.appendleft(''.join(palavra))

    return ' '.join(palavras)
    

def invertePalavras(str_):
    """
    Desenvolva a função `invertePalavras` que recebe uma string e
    devolve uma nova string com todas as palavras por ordem inversa. 
    Assuma que as palavras estão separadas apenas por um espaço.
    """
    return ' '.join(reversed(str_.split()))

#######################################################################
## SUBSTITUI
#######################################################################

def substitui1(str1, str2, str3):    
    """
    Substitui em `str1` todas as ocorrências de `str2` por `str3`.  
    Os caracteres da string são acumulados numa lista que depois é 
    transformada numa string com `str.join`. Esta versão utiliza 
    `str.find` c/ slicing para extrair partes da string.
    """
    if len(str1) < len(str2) or len(str2) == 0:
        return str1

    lstr1 = []
    i = 0
    while True:
        j = str1.find(str2, i) 
        if j == -1:
            break
        lstr1.extend(str1[i:j])
        lstr1.extend(str3)
        i = j + len(str2)
    lstr1.extend(str1[i:])        
    return ''.join(lstr1)


def substitui2(str1, str2, str3):    
    """
    Substitui em `str1` todas as ocorrências de `str2` por `str3`.  
    Os caracteres da string são acumulados numa lista que depois é 
    transformada numa string com `str.join`. Esta versão utiliza 
    `str.find`.
    Os caracteres são copiados um-a-um de str1 para o destino.    
    """
    if len(str1) < len(str2) or len(str2) == 0:
        return str1

    lstr1 = []
    i = 0
    while i < len(str1):
        if str1.find(str2, i, i + len(str2)) != -1:
            lstr1.extend(str3)
            i += len(str2)
        else:
            lstr1.append(str1[i])
            i += 1
    return ''.join(lstr1)   


def substitui3(str1, str2, str3):
    """
    Substitui em `str1` todas as ocorrências de `str2` por `str3`.  
    Os caracteres da string são acumulados numa lista que depois é 
    transformada numa string com str.join. Esta versão não utiliza 
    qualquer método da classe str, nem sequer str.find.    
    Os caracteres são copiados um-a-um de str1 para o destino.
    """
    if len(str1) < len(str2) or len(str2) == 0:
        return str1

    lstr1 = []
    i = 0
    while i < len(str1):
        if str1[i] == str2[0]:
            # Se o caractere actual de str1 é igual ao primeiro de 
            # str2, vamos verificar os restantes para ver se str2 está 
            # dentro de str1 a partir de i+1.
            # j: indice p/ str1 a partir do caractere i+1 (i não varia)
            # k: indíce p/ str2 (começa em 1 pq já vimos o carac. 0)
            j, k = i + 1, 1
            while k < len(str2) and str1[j] == str2[k]:
                j += 1
                k += 1

            if k == len(str2):
                # Como k percorreu str2 até ao fim, então todos os 
                # caracteres de str2 estão contidos em str1 a partir 
                # do valor actual de i. Vamos acrescentar str3 a lstr1. 
                # Nenhum caractere de str2 passa para str1. Como str2 
                # já foi substituída, i avança para o caractere de str1 
                # que vem depois de str2 e continuamos a partir daí. 
                lstr1.extend(str3)
                i += len(str2)
                continue 

        lstr1.append(str1[i])
        i += 1
    return ''.join(lstr1)


def substitui(str1, str2, str3):
    """
    Substitui em `str1` todas as ocorrências de `str2` por `str3`.  
    """
    if len(str1) < len(str2) or len(str2) == 0:
        return str1
    return str3.join(str1.split(str2))

#######################################################################
## REMOVEWHITE
#######################################################################

def removeWhite(str_):
    """
    Desenvolva a função removeWhite que remove todos os caracteres 
    "brancos" (espaços, nova linha, tabs, etc.) de uma string.
    """
    return ''.join(str_.split())

#######################################################################
## MONTHNAME
#######################################################################

import datetime as dtm

def monthName(monthOrDate, abbrev=True):
    """
    Desenvolva a função `monthName` que pode receber um número de mês 
    - de 1 a 12 - ou uma data - ie, um objecto do tipo date ou datetime -
    e devolve o nome do mês. Se a função não receber nenhum argumento, 
    devolve o nome do mês actual. 
    Se o parâmetro `abbrev` for True, devolve o nome abreviado 
    em vez de completo (exemplo: `Jan` vs. `Janeiro`).
    Ignore os dados de localização (quer isto dizer que devolve o 
    nome do mês para o `locale` que estiver definido no momento).
    """
    dt = monthOrDate
    if isinstance(monthOrDate, int):
        dt = dtm.date(1, monthOrDate, 1)
    return dt.strftime("%b" if abbrev else "%B")

#######################################################################
## RANDLETTER e RANDLETTERS
#######################################################################

import random

def randLetter(type_=''):
    """
    Desenvolva a função randLetter que selecciona aleatoriamente uma 
    letra e devolve-a. Esta função deverá possuir um parâmetro opcional 
    `type_` que indica a randLetter que tipo de letra deve seleccionar: 
    se for 'U' escolhe uma letra maiúscula; se for 'L', escolhe uma 
    minúscula; para qualquer outro valor de `type_`, randLetter escolhe 
    uma letra tendo em conta as duas categorias de valores. Por omissão 
    `type_` tem o valor '' (string vazia) o que indica que pode devolver 
    uma letra maiúscula ou minúscula.    
    """
    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    both = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    sel = lower if type_ == 'L' else upper if type_ == 'U' else both
    return sel[random.randint(0, len(sel)-1)]


def randLetters(n=2, type_=''):
    """
    Desenvolva a função randLetters que devolve uma string com letras 
    seleccionadas aleatoriamente. Possui dois parâmetros: `n`, que 
    indica quantas letras terá a string, e `type_` (ver randLetter). 
    Por omissão, n tem o valor 2 e `type_` tem o valor ''.
    """
    return ''.join([randLetter(type_) for i in range(n)])
