"""
LABORATÓRIO 4 - Classes e Programação Orientada por Objectos

Exemplo clássico com contas bancárias para ilustrar os conceitos de 
herança e polimorfismo (com classes). Neste módulo desenvolvemos várias 
classes para representar quatro diferentes tipos de contas bancárias: 
à ordem, ordenado, a prazo e poupança-habitação.

As classes relacionam-se através de herança:

Conta
 |
 +----> Ordem
 |       |
 |       +--- Ordenado
 | 
 +----> Prazo
         |
         +----> PoupancaHabitacao

"""

from decimal import Decimal
from datetime import date
from enum import Enum


EstadoConta = Enum('EstadoConta', 'ABERTA ENCERRADA BLOQUEADA INACTIVA')


DATE_FMT = '%Y-%m-%d'


class ContaBancaria:

    def __init__(
            self, 
            num_cliente, 
            saldo,
            num_conta=None,
            data_abertura=None,
            estado=EstadoConta.ABERTA,
    ):
        if saldo < self.saldo_min:
            raise ValueError("Saldo inicial %.2f inválido!" % saldo)

        if data_abertura and data_abertura < ContaBancaria.DATA_INICIAL:
            raise ValueError("Data %s inválida!" % data_abertura)        

        if estado not in EstadoConta:
            raise ValueError("Estado inicial da conta %s inválido!" % estado)

        self.num_cliente = num_cliente
        self._saldo = saldo
        if num_conta:
            self.num_conta = num_conta
        else:
            self.num_conta = ContaBancaria.prox_num_conta
            ContaBancaria.prox_num_conta += 1
        self.data_abertura = data_abertura if data_abertura else date.today()
        self.estado = estado

    @property
    def duracao(self):
        return (date.today() - self.data_abertura).days
  
    @property
    def saldo(self):
        raise NotImplementedError()

    def depositar(self, montante):
        # Versão incorrecta para contas a prazo (e derivadas) para 
        # evitar tornar este código demonstrativo mais complexo
        if montante < 0:
            raise ValueError("Montante %.2f inválido!" % montante)
        self._saldo += montante
        return self.saldo

    def __str__(self):
        return ','.join((
            str(self.num_conta),
            str(self.num_cliente),
            self.__class__.__name__,
            "%.2f" % self.saldo,
            self.data_abertura.strftime(DATE_FMT),
            self.estado.name,
        ))

    def __repr__(self):
        txt = '\n  '.join(self._attrsReprs())
        return "%s(\n  %s\n)" % (self.__class__.__name__, txt)

    def _attrsReprs(self):
        return [
            "num_conta=%r," % self.num_conta,
            "num_cliente=%r," % self.num_cliente,
            "saldo=%r," % self.saldo,
            "data_abertura=%r," % self.data_abertura,
            "estado=%s," % self.estado,
        ]

    DATA_INICIAL = date(1997, 5, 5)
    prox_num_conta = 117
    saldo_min = 0


class ContaOrdem(ContaBancaria):

    @property
    def saldo(self):
        return self._saldo

    def levantar(self, montante):
        if montante < 0:
            raise ValueError("Montante %.2f inválido!" % montante)
        if self._saldo < montante:
            raise ValueError("Saldo insuficiente %.2f" % self._saldo)
        self._saldo -= montante


class ContaOrdenado(ContaOrdem):    

    def __init__(self, ordenado, *args_pos, **args_com_nome):
        if ordenado <= 0:
            raise ValueError("Ordenado %.2f inválido!" % ordenado)
        super().__init__(*args_pos, **args_com_nome)
        self.ordenado = ordenado

    def levantar(self, montante):
        if montante < 0:
            raise ValueError("Montante %.2f inválido!" % montante)
        novo_saldo = self._saldo - montante
        if novo_saldo < -self.ordenado:
            raise ValueError("Saldo insuficiente %.2f" % self._saldo)
        self._saldo -= montante

    def __str__(self):
        txt = super().__str__()
        return txt + (",%.2f" % self.ordenado) 

    def _attrsReprs(self):
        fields = super()._attrsReprs()
        fields.append("ordenado=%s," % self.ordenado)
        return fields


class ContaPrazo(ContaBancaria):

    def __init__(self, taxa_juro, *args_pos, **args_com_nome):        
        if taxa_juro < 0:
            raise ValueError("Taxa de juro %.2f inválida!" % taxa_juro)
        super().__init__(*args_pos, **args_com_nome)
        self.taxa_juro = taxa_juro/100

    @property
    def saldo(self):
        if self.duracao < self.duracao_min:
            return self._saldo
        dias = Decimal(self.duracao)
        return self._saldo * (1 + ((dias/365)*self.taxa_juro))

    def levantar(self, montante):
        if montante < 0:
            raise ValueError("Montante %.2f inválido!" % montante)

        if self.duracao < self.duracao_min:
            raise ValueError("Prazo mínimo %s dias ainda não atingido!" 
                             % self.duracao_min)

        novo_saldo_com_juros = self.saldo - montante
        if novo_saldo_com_juros < self.saldo_min:
            raise ValueError("Saldo final %.2f inferior ao saldo mínimo %.2f!"
                             % (novo_saldo_com_juros, self.saldo_min))

        montante_sem_juros = montante / (1+self.taxa_juro)
        novo_saldo_sem_juros = self._saldo - montante_sem_juros
        self._saldo = novo_saldo_sem_juros
        return self.saldo

    def __str__(self):
        txt = super().__str__()
        return txt + (",%.2f" % (self.taxa_juro*100)) 

    def _attrsReprs(self):
        fields = super()._attrsReprs()
        fields.append("taxa_juro=%r," % (self.taxa_juro*100))
        return fields

    duracao_min = int(0.25*365)
    saldo_min = 100


class ContaPoupancaHabitacao(ContaPrazo):
    duracao_min = 18*365
    saldo_min = 150


c1 = ContaOrdem(
    num_cliente=1,
    saldo=Decimal('1500'),
    data_abertura=date(2014, 1, 5),
)

c2 = ContaOrdenado(
    num_cliente=2, 
    saldo=Decimal('150'),
    ordenado=Decimal('750'),
    data_abertura=date(2015, 5, 5),
)

c3 = ContaPrazo(
    num_cliente=1,
    saldo=Decimal('1500'),
    data_abertura=date(2014, 1, 5),
    taxa_juro=Decimal('2.00'),
)

c4 = ContaPoupancaHabitacao(
    num_cliente=1,
    saldo=Decimal('1500'),
    data_abertura=date(2014, 1, 5),
    taxa_juro=Decimal('2.00'),
)


contas = [
    ContaOrdenado(
        num_cliente=1, 
        saldo=Decimal('100'), 
        ordenado=Decimal('1680')
    ),
    ContaOrdenado(
        num_cliente=2, 
        saldo=Decimal('150'),
        ordenado=Decimal('750')
    ),
    ContaOrdem(
        num_cliente=1, 
        saldo=Decimal('190'),
    ),
    ContaPrazo(
        num_cliente=1,
        saldo=Decimal('1500'),
        data_abertura=date(2014, 1, 7),
        taxa_juro=Decimal('1.5'),
    ),
    ContaOrdem(
        num_cliente=3, 
        saldo=Decimal('750')        
    ),
    ContaPoupancaHabitacao(
        num_cliente=2, 
        saldo=Decimal('1375'),
        data_abertura=date(2009, 1, 7),
        taxa_juro=Decimal('2.75'),
    ),
]

total = 0
for conta in contas:
    total += conta.saldo

total = sum(conta.saldo for conta in contas)

double total = 0;
for (ContaBancaria conta : contas) {
    total += conta.get_saldo();
}

# class A:
#
#     def __init__(self, x, y=3):
#         self.x = x
#         self.y = y
#         print('A x:', x)
#         print('A y:', y)
#
#     def __repr__(self):
#         return self.__class__.__name__ + ' ' + str(self.x) + ',' + str(self.y)


# class B(A):
#
#     def __init__(self, *args, z=3, **kargs):
#         super().__init__(*args, **kargs)
#         self.z = z
#         print('B z:', z)
#
#     def __repr__(self):
#         txt = super().__repr__()
#         txt += ',' + str(self.z)
#         return txt

# def f(a, *args, b=10, **kargs):
#     print("a:", a, "  args:", args, "  b:", b,  "  kargs:", kargs)

# >>> f(1, 3, 4, 5, c=15)
# a: 1   args: (3, 4, 5)   b: 10   kargs: {'c': 15}
# >>> f(1, 3, 4, 5, c=15, b=19)
# a: 1   args: (3, 4, 5)   b: 19   kargs: {'c': 15}
