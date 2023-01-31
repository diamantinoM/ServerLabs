"""
LABORATÓRIO 4

Exemplos e teoria sobre alguns dos conceitos que estão na base da 
Programação Orientada por Objectos (POO).
"""

import math

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
# INTRODUÇÃO

Neste laboratório vamos introduzir alguns conceitos que depois serão
importantes para contextualizar o paradigma de programação designado de 
"Programação Orientada por/a Objectos" (POO). Esses conceitos são:
- Abstracção
- Abstracção Procedimental 
- Definição de Objectos de Dados Compostos
- Abstracção de Dados
- Barreiras de Abstracção
- Operações Genéricas
- Expedir/Despachar por Tipo
- Programação Orientada pelos Dados

Os conceitos serão introduzidos através de dois exemplos:
- manipulação de números racionais/fracções e de números complexos
- codificação e descodificação de bytes para variadas aplicações

Também faremos alusão a outros exemplos sempre que necessário.

Inicialmente utilizaremos os mecanismos da linguagem Python dados até 
agora para introduzir estes conceitos. Através deste caminho chegaremos
então à POO e ao mecanismo por excelência da linguagem Python para lidar
com estes conceitos: a classe.

# ABSTRAÇÃO, DADOS COMPOSTOS, ABSTRAÇÃO DE DADOS

Vamos começar por introduzir um método para concepção de programas
- abstração de dados (data abstraction) - e um mecanismo para 
organização dos dados manipulados por esses programas - definição de
dados compostos (compound data). 

Nestes exemplos e nos seguintes, vamos utilizar bastante o termo 
abstracção, noção muito importante em programação. Fica aqui uma 
passagem do livro 'Programação em Python - Introdução à Programação 
Utilizando Múltiplos Paradigmas' (PP-IPUMP) que menciona abstração e 
depois particulariza para o caso da abstração procedimental, forma de 
abstração que introduzimos em laboratórios anteriores:

"10.1 - A abstracção em programação

Sabemos que uma abstracção é uma descriçao ou uma especificação 
simplificada de uma entidade que dá ênfase a certas propriedades dessa 
entidade e ignora outras. Uma boa abstracção especifica as propriedades 
importantes e ignora os pormenores. Uma vez que as propriedades 
relevantes de uma entidade dependem da utilização a fazer com essa 
entidade, o termo "boa abstracção" está sempre associado a uma 
utilização particular da entidade.

A abstracção é um conceito essencial em programação. De facto, a 
actividade de programação pode ser considerada como a construção de 
abstracções que podem ser executadas por um computador.

Até aqui temos usado a abstracção procedimental para a criação de 
funções. Usando a abstracção procedimental, os pormenores da realização 
de uma função podem ser ignorados, fazendo com que uma função possa ser 
substituída por uma outra função com o mesmo comportamento global, 
utilizando um outro algoritmo, sem que os programas que utilizam essa 
função sejam afectados. A abstracção procedimental permite pois separar 
o modo como uma função  é utilizada do modo como essa função é 
realizada."

As linguagens de programação fornecem-nos um conjunto de tipos de dados
de dados primitivos através dos quais criamos e manipulamos objectos de 
dados como números inteiros, strings de caracteres, ou valores 
booleanos. Apenas estes objectos primitivos, por si, de forma isolada, 
não são suficientes para representamos os "conceitos" fazem parte do 
domínio das aplicações que vamos desenvolver. Nesse sentido, encontramos
nessas linguagens mecanismos para definirmos novos "conceitos". 

Uma forma rudimentar de representar estes conceitos passa por recorrer 
às estruturas de dados que fazem parte da linguagem. Por exemplo,
suponhamos que queremos representar um Livro no contexto de uma 
aplicação de gestão de livrarias. Depois de definirmos os atributos que 
nos interessa manipular (eg, o título do livro, os autores, o género, 
o isbn, etc.), podemos utilizar um dicionário ou uma lista para agregar
os valores dos atributos de um determinado livro. Noutros casos, porém, 
as linguagens fornecem mecanismos mais sofisticados para definirmos 
objectos de dados compostos. Estes envolvem a criação de novos tipos 
de dados, utilizando para tal classes ou mecanismos derivados.

Tal como a definição de procedimentos e funções permite-nos definir 
processos conceptualmente mais sofisticados e mais próximos do domínio 
da aplicação que queremos modelar, os mecanismos para construir objectos
de dados compostos possibilitam trabalhar a informação a um nível 
conceptual mais elevado. 

A utilização de dados compostos aumenta a modularidade dos nossos 
programas. Num dos exemplos que veremos a seguir - cálculo com números
racionais - ao representarmos um número racional como um objecto da
linguagem, então podemos separar as partes do nosso programa que lidam
com números racionais, dos detalhes relacionados com a representação
desses números racionais. Esta técnica de isolar as partes de um
programa que lidam com a representação "física" dos objectos de dados 
das partes que lidam com a utilização desses objectos é um método muito 
poderoso para desenho e concepção de programas, sendo designado de 
abstracção de dados.

A ideia subjacente à abstração de dados consiste em fazer com que as
partes que utilizam os objectos de dados compostos, o façam assumindo o
minímo possível a respeito da representação desses mesmos objectos. Por
seu turno, as partes responsáveis por representar esses objectos, 
isto é, por implementá-los fazem-no independentemente dos programas 
que vão necessitar desses mesmos objectos. A interface entre essas
duas partes é feita através de um conjunto de funções e procedimentos
designados de construtores e selectores ou acessores. Estas funções
e procedimentos é que estabelecem uma barreira entre a abstração
e a implementação. Além de construtores e selectores, podemos também 
acrescentar outras funções/procedimentos designados de modificadores e 
destrutores. Não nos vamos preocupar com definições concretas, mas os 
nomes já dão a enteder o propósito dessas funções/procedimentos.

Os exemplos que se seguem permitem ilustrar como abstração de dados 
torna os programas mais fáceis de conceber, manter e modificar. Citando,
novamente PP-IPUMP:

"O conceito equivalente à abstracção procedimental para dados (ou 
estruturas de informação) tem o nome de abstracção de dados. A abstracção
de dados é uma metodologia que permite separar o modo como uma estrutura 
de informação é utilizada dos pormenores relacionados com o modo como 
essa estrutura de informação é construída a partir de outras estruturas
de informação. Quando utilizamos um tipo de informação embutido em 
Python, por exemplo uma lista, não sabemos (nem queremos saber) qual o 
modo como o Python realiza internamente as listas. Para isso, recorremos
a um conjunto de operações embutidas (apresentadas na Tabela 5.1) para 
escrever as nossas funções. Se numa versão posterior do Python, a 
representação interna das listas for alterada, os nossos programas não 
são afectados por essa alteração. A abstracção de dados permite a 
obtenção de um comportamento semelhante para os dados criados no nosso 
programa. Analogamente ao que acontece quando recorremos à abstracção 
procedimental, com a abstracção de dados, podemos substituir uma 
realização par- ticular da entidade correspondente a um dado sem ter de 
alterar o programa que utiliza essa entidade, desde que a nova realização
da entidade apresente o mesmo comportamento genérico, ou seja, desde que 
a nova realização corresponda, na realidade, à mesma entidade abstracta."

# EXEMPLO 1.1: NÚMEROS RACIONAIS

Vamos supor que pretendemos fazer cálculos com números racionais. 
Queremos calcular o resultado de expressões e obter resultados como:

   1      2     11            1     1     3           4     11     22
  ———  + ——— = ————    ou    ——— + ——— = ———    ou   ——— * ———— = ————
   4      3     12            2     4     4           5     6      15

Note-se que queremos obter 11/12, 3/4 e 22/15, e não 0.91(6), 0.75 ou 
1.4(6). Ou seja, as operações aritméticas elementares entre números 
racionais devem produzir também número racionais. 

Queremos, então, ser capazes de somar, subtrair, multiplicar e dividir
números racionais. Também nos interessa poder testar se dois números
racionais são iguais, diferentes, se um deles é maior, maior ou igual,
menor, ou menor ou igual do que o outro.

Idealmente, gostávamos de poder ter uma representação literal para 
estes números. Por exemplo, algo como '7/2_r' para indicar sete meios. 
Em C++, linguagem que suporta literais definidos pelos utilizadores, 
tal seria perfeitamente possível. Em Python apenas podemos utilizar
construtores.

Em termos das operações fundamentais para manipulação de racionais, 
começamos por assumir que as seguintes operações estão definidas:

- RAT(<N>, <D>): construtor que devolve o número racional cujo 
  numerador é <N> e cujo denominador é <D>
- NUMER(<R>): selector que devolve o numerador do número racional <R>
- DENOM(<R>): selector que devolve o denominador do número racional <R>

Pois bem, mesmo não tendo definido estas operações podemos já pensar 
nas restantes que se implementam em função destas. As operações de soma,
subtração, multiplicação, divisão, teste de igualdade e teste de 
diferença dependem das seguintes relações:

   n₁     n2      n1*d2 + n2*d1
  ———— + ————  = ———————————————
   d₁     d2          d1*d2

   n1     n2      n1*d2 - n2*d1
  ———— - ————  = ————————————————
   d1     d2          d1*d2

   n1     n2      n1*n2
  ———— * ————  = ———————
   d1     d2      d1*d2

   n1     n2      n1*d2
  ———— / ————  = ———————
   d1     d2      d1*n2

   n1     n2   
  ———— = ————  <=> n1*d2 = n2*d1 
   d1     d2   

   n1         n2   
  ———— not = ———— <=> not (n1*d2 = n2*d1)  (negação da igualdade é verdadeira)
   d1         d2  
"""

def add_rat(x, y):
    return rat(numer(x)*denom(y) + numer(y)*denom(x), denom(x) * denom(y))
   

def sub_rat(x, y):
    return rat(numer(x)*denom(y) - numer(y)*denom(x), denom(x) * denom(y))


def mul_rat(x, y):
    return rat(numer(x) * numer(y), denom(x) * denom(y))


def div_rat(x, y):
    return rat(numer(x) * denom(y), denom(x) * numer(y))


def pow_rat(b, e):
    return rat(numer(b) ** e, denom(b) ** e)


def eq_rat(x, y):
    return numer(x) * denom(y) == numer(y) * denom(x)


def neq_rat(x, y):
    return not eq_rat(x, y)


def gt_rat(x, y):
    return numer(x) * denom(y) > numer(y) * denom(x)


def ge_rat(x, y):
    return gt_rat(x, y) or eq_rat(x, y)


def lt_rat(x, y):
    return not ge_rat(x, y)


def le_rat(x, y):
    return not gt_rat(x, y)


def rat_to_str(x):
    return f'{numer(x)}/{denom(x)}'

"""
Vamos agora definir o construtor 'rat' e os acessores 'numer' e 'denom'.
Todo o nosso sistema de manipulação de números racionais assenta nestes
métodos elementares.
"""

# def rat(n: int, d: int):
#     return (n, d)

def rat(n: int, d: int):
    if d == 0:
        raise ValueError('math domain error')
    g = math.gcd(n, d)
    return (n // g, d // g)


def numer(x):
    return x[0]


def denom(x):
    return x[1]

"""
Como vimos, o propósito da abstração de dados passa por separar o 
código que utiliza objectos de dados compostos do código que representa
esses objectos (ie, que dá uma estrutura aos atributos que constituem 
esses objectos). 
A separar essas partes, ou esses módulos, temos então o que podemos 
visualizar como uma barreira de abstração. O código que utiliza a 
a abstração de dados, no nosso caso, os números racionais construídos
com rat, fazem-no apenas através de um conjunto de procedimentos 
para "consumo público": 'add_rat', 'sub_rat', 'mul_rat', etc. Por seu 
turno estes procedimentos foram implementados em termos de 'rat', 
'numer' e 'denom', os quais foram implementados em termos de tuplos.

        Programa que efectua aritmética com números racionais
  ________________________________________________________________
      ADD_RAT  │  SUB_RAT  │  MUL_RAT  │  DIV_RAT │ EQ_RAT │ ...
  ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
        Números racionais enquanto numeradores e denominadores
  ________________________________________________________________
                RAT  │  NUMER  │  DENOM 
  ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
            Par de números inteiros agregados num tuplo
  ________________________________________________________________
                TUPLE  │  [ ]  │  [::]  |  LEN  │  etc.
  ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
            Representação de um tuplo em Python

Para reforçar o princípio da abstração de dados, aqui fica uma 
implementação dos métodos acessores para números racionais. Desta
vez, eles vão ser implementados através de um objecto de dados composto 
que designamos de 'pair'. Um 'pair' é, na verdade, uma closure que 
memoriza e permite o acesso aos dois elementos de um par de elementos: 
'first' e 'second'. Começamos por ilustrar a implementação deste novo 
objecto de dados composto.
"""

def make_pair(first, second):
    def pair(index):
        if index not in (0, 1):
            raise ValueError('Invalid index to pair: ' + index)
        return first if index == 0 else second
    return pair

# Se ignorássemos a detecção de erros, então make_pair poderia 
# simplesmente devolver uma lambda
# def make_pair (f, s):
#    return lambda index: first if index == 0 else second


def first(pair):
    return pair(0)


def second(pair):
    return pair(1)


# def rat(n: int, d: int):
#     if d == 0:
#         raise ValueError('math domain error')
#     g = math.gcd(n, d)
#     return make_pair(n//g, d//g)


# def numer(x):
#     return first(x)


# def denom(x):
#     return second(x)

"""
# EXEMPLO 1.2: ABSTRAÇÃO DE DADOS COM NÚMEROS COMPLEXOS

Os números complexos são muito utilizados em matemática, ciência e 
engenharia, entre outras disciplinas técnicas. 
(ver: https://en.wikipedia.org/wiki/Complex_number)

São escritos na forma "a + bi", onde 'a' e 'b' são números reais e 'i'
representa a solução para a equação 'i² = -1' (ou seja, 'i = √‾-1'). Como 
não existe solução real para esta equação, 'i' é designado de número 
imaginário. A parcela 'bi' é designada de parte imaginária, ao passo que 
a parcela 'a' é designada de parte real. Um número imaginário com parte
real 0 (ou seja, 'a' = 0) é um número complexo puro. Podemos olhar para
um número complexo como sendo um par de coeficientes reais, um pouco à
semelhança dos números racionais. Geometricamente, o conjunto de
números complexos um número complexo pode ser representado num plano 
bidimensional:

        Im 
           ∧
           │
         b │.....* z = a + bi = r (cosφ + i sinφ)
           │    /. 
           │   / .     r: magnitude/módulo  r = √‾(a² + b²)   a = r cosφ
           │  /r .     φ: ângulo            φ = arctan(b, a)  b = r sinφ
           │ /   .                        
           │/φ)  .                        
    ───────┼──────────────────────────────>
         0 │     a                         Re
           │

O eixo dos XX é designado de eixo Real ou Re, ao passo que ao eixo dos 
YY chamamos de eixo Imaginário ou Im. 'r' é a magnitude do número 
complexo 'z' e 'φ' (letra grega minúscula 'phi') o ângulo com o eixo Re. 
A magnitude de um número complexo, 'r', é também designada de módulo do 
número e representado por '|z|' ('z' é o número complexo em questão).

Como observamos na figura, um número complexo também pode ser expresso
através do ângulo 'φ' e da sua magnitude 'r', por meio da expressão
"r (cosφ + i sinφ)". Designa-se esta representação por *forma polar*.
À representação "a + bi", isto é, em função das coordenadas no plano
bidimensional 'a' e 'b', damos o nome de *forma rectangular* (ou *forma
forma cartesiana*). Sabendo 'a' e 'b' podemos obter 'r' e 'φ' e 
vice-versa.

Dados dois números complexos "z₁ = a + bi" e "z₂ = c + di" (ou seja, 
em forma rectangular), as operações aritméticas e relacionais são
definidas por:

    z₁ + z₂ = (a + c) + (b + d)i

    z₁ - z₂ = (a - c) + (b - d)i

    z₁ * z₂ = (ac - bd) + (ad + bc)i        [1]

    z₁      ac + bd     bc - ad
   ———— =  ————————— + ————————— i          [1]
    z₂      c² + d²     c² + d²    

   z₁ = z₂ <=> a = c and b = d 

   z₁ⁿ -> converter para forma polar e depois ver em baixo

[1] - Na prática, convertem-se ambos os números para forma polar e 
      depois faz-se a multiplicação/divisão.

Dados os mesmos números z1 e z2 em forma polar - z₁ =  r(cosφ + i sinφ)
e z₂ =  s(cosθ + i sinθ) - as mesmas operações aritméticas e relacionais
são assim definidas:

    z₁ + z₂ = r cosφ + s cosθ + i (r sinφ + s sinθ)   [2]

    z₁ - z₂ = expressão similar à anterior            [2]

    z₁ * z₂ = rs (cos(φ+θ) + i sin(φ+θ))              [3]

    z₁     r
   ———— = ——— (cos(φ-θ) + i sin(φ-θ))                 [3]
    z₂     s

    z₁ = z₂ <=> r = s and φ = θ 

    z₁ⁿ = rⁿ(cos(nφ) + i sin(nφ))                     [4]

[2] - Na prática convertem-se ambos os números para forma rectangular e 
      depois faz-se a soma/subtracção

[3] - Ou seja, a magnitude do novo número complexo z₃ que resulta de 
      multiplicar z₁ por z₂ é o produto das magnitudes, ao passo que o 
      ângulo é simplesmente a soma dos ângulos de z₁ e z₂. Se na frase
      anterior trocarmos 'produto' por 'divisão' e 'soma' por 
      'diferença', então sabemos como obter o número complexo z₃ que 
      resulta da divisão de z₁ por z₂.

[4] - Apenas necessitamos de elevar a magnitude a 'n' e multiplicar o 
      ângulo por 'n'. 
     
Em termos de desempenho das operações matemáticas com números complexos, 
as duas formas de representação, rectangular ou polar, possuem vantagens 
e desvantagens. Multiplicações, divisões, potências, logaritmos e 
operações trignométricas em geral, são mais fáceis em notação polar. 
Somas, subtracções, escalonamentos, translações, etc., são mais fáceis 
em notação rectangular. Assim, um objectivo interessante passa por 
desenvolver um sistema que execute operações aritméticas com números 
complexos, independentemente da forma utilizada. Aliás, tendo em conta 
o princípio da abstração de dados, as operações aritméticas para números 
complexos não devem depender da representação em concreto. Mais: por 
vezes queremos obter a magnitude de um número complexo expresso na forma
rectangular, tal como também é útil extrair a parte real de um número 
complexo em forma polar.

Como vimos com os números racionais, utilizando abstração de dados
podemos implementar essas operações e fazer com que não dependam da
representação em concreto de um número complexo. Sabemos que, com os
construtores e selectores apropriados, podemos operar sobre uma 
representação abstracta. Porém, agora queremos fazer coexistir duas 
representações concretas em simultâneo e, de alguma forma, as operações 
aritméticas vão ter que "agulhar" para essas representações concretas.
Ou seja, além de uma barreira de abstração horizontal a isolar as 
operações aritméticas das representações concretas, necessitamos de uma
barreira de abstração vertical, que permita que as duas representações
não interfiram uma com a outra, mas que seja possível transformar um 
número em forma rectangular no número equivalente em forma polar.

        Programa que efectua aritmética com números complexos
  ______________________________________________________________________
    ADD_COMPLEX  │  SUB_COMPLEX  │  MUL_COMPLEX  │  DIV_COMPLEX │  ...
  ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
        Números complexos dos quais se consegue extrair uma parte 
        real, uma parte imaginária, um ângulo e uma magnitude
  ______________________________________________________________________
        REPRESENTAÇÃO             │        REPRESENTAÇÃO 
        RECTANGULAR               │        POLAR
  ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
        Estrutura de dados da linguagem que suporta o objecto de 
        dados composto (eg, um tuplo)

Neste exemplo vamos ilustrar novamente o princípio de abstração de dados
com números complexos. No exemplo seguinte dedicamo-nos, então, à 
questão de suportar as duas representações, rectangular e polar, em 
simultâneo por meio de Operações Genéricas com Despacho p/ Tipo ou 
pr via de Programação Orientada pelos Dados.

Em termos das operações fundamentais para manipulação de complexos em
ambas as formas, vamos por assumir que as seguintes operações estão 
definidas:

- COMPLEX_FROM_REAL_IMAG(<R>, <I>): devolve um número complexo a partir
  das coordenadas/partes real <R> e imaginária <I>                     

- COMPLEX_FROM_MAG_ANGLE(<M>, <A>): devolve um número complexo a partir 
  das coordenadas polares, isto é, a partir da magnitude <M> e do 
  ângulo <A> (em radianos)

- REAL_PART(<Z>): selector que devolve a parte real do número 
  complexo <Z>

- IMAG_PART(<Z>): selector que devolve a parte imaginária do número 
  complexo <Z>

- MAGNITUDE(<Z>): selector que devolve a magnitude do número complexo <Z>

- ANGLE(<Z>): selector que devolve o ângulo do número complexo <Z>
  
É de notar que estas operações elementares devem estar definidas para
ambas as formas, rectangular e polar, conforme veremos.

Pois bem, mesmo não tendo definido as operações elementares, podemos já 
pensar nas restantes operações aritméticas. Como vimos nas fórmulas em 
cima exibidas, podemos somar e subtrair números complexos em termos das
suas partes reais e imaginárias, enquanto que é mais natural implementar
a multiplicação e a divisão em termos das suas magnitudes e ângulos.
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
Implementação de números complexos na forma rectangular ou cartesiana.
Deve ser possível fazer um número rectangular a partir de coordenadas
cartesianas (isto é, das partes real e imaginária) e de coordenadas
polares (ou seja, a partir de uma magnitude e de um ângulo).

As partes real e imaginária são armazenados num tuplo de dois elementos.

def real_part(z):
    return z[0]


def imag_part(z):
    return z[1]


def magnitude(z):
    return math.sqrt(real_part(z)**2 + imag_part(z) ** 2)


def angle(z):
    return math.atan2(imag_part(z), real_part(z))


def complex_from_real_imag(r, i):   # r -> parte real   i -> parte imaginária
    return (r, i)


def complex_from_mag_angle(m, a):   # m -> magnitude   a -> angulo
    return complex_from_real_imag(m * math.cos(a), m * math.sin(a))
"""

"""
Implementação de números complexos na forma polar.

À semelhança da implementação anterior, as coordenadas polares são
armazenados num tuplo de dois elementos.
"""

def real_part(z):
    return magnitude(z) * math.cos(angle(z))


def imag_part(z):
    return magnitude(z) * math.sin(angle(z))


def magnitude(z):
    return z[0]


def angle(z):
    return z[1]


def complex_from_real_imag(r, i):
    return complex_from_mag_angle(math.sqrt(r**2 + i**2), math.atan2(i, r))


def complex_from_mag_angle(m, a):
    return (m, a)


