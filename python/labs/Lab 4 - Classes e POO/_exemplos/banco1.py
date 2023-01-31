"""
LABORATÓRIO 4 - Classes e Programação Orientada por Objectos

Exemplo clássico com contas bancárias para ilustrar os conceitos de 
herança e polimorfismo (com classes). Neste módulo desenvolvemos a 
classe `Conta` para representar, na verdade, quatro tipo de contas 
diferentes: à ordem, ordenado, a prazo e poupança-habitação.

Neste módulo ainda não utilizamos herança nem poliformismo, optando
antes por enquadrar a utilidade desses mecanismos ao proporcionar uma
solução complicada, que tem que lidar com muitos casos especiais.
"""

from decimal import Decimal
from datetime import date
from enum import Enum


TipoConta = Enum('TipoConta', 'ORDEM ORDENADO PRAZO POUPANCA_HABITACAO')


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
            tipo=TipoConta.ORDEM,
            ordenado=Decimal('0.00'),
            taxa_juro=Decimal('0.00'),
    ):
        # Validações comuns
        if saldo < 0:
            raise ValueError("Saldo inicial %.2f inválido!" % saldo)

        if data_abertura and data_abertura < ContaBancaria.DATA_INICIAL:
            raise ValueError("Data %s inválida!" % data_abertura)        

        if estado not in EstadoConta:
            raise ValueError("Estado inicial da conta %s inválido!" % estado)

        if tipo not in TipoConta:
            raise ValueError("Tipo de conta %s inválido!" % tipo)

        # Validações conta à ORDEM e ORDENADO
        if tipo in (TipoConta.ORDENADO,) and ordenado <= 0:
            raise ValueError("Ordenado %.2f inválido!" % ordenado)

        if tipo not in (TipoConta.ORDENADO,) and ordenado != 0:
            raise ValueError("Valor de ordenado %.2f inválido para este "
                             "tipo de conta %s!" % (ordenado, tipo))

        # Validações conta a PRAZO e POUPANCA_HABITACAO
        conta_com_juros = tipo in (TipoConta.PRAZO, TipoConta.POUPANCA_HABITACAO)
        poup_hab = tipo is TipoConta.POUPANCA_HABITACAO
        prazo = tipo is TipoConta.PRAZO

        if taxa_juro <= 0 and conta_com_juros:           
            raise ValueError("Valor de juro %.2f inválido para este "
                             "tipo de conta %s!" % (taxa_juro, tipo))

        montante_min = ((poup_hab and ContaBancaria.saldo_min_phab) or
                        (prazo and ContaBancaria.saldo_min_prazo))
        if conta_com_juros and saldo < montante_min:
            raise ValueError("Saldo %.2f inválido para este "
                             "tipo de conta %s!" % (saldo, tipo))

        self.num_cliente = num_cliente
        self._saldo = saldo
        if num_conta:
            self.num_conta = num_conta
        else:
            self.num_conta = ContaBancaria.prox_num_conta
            ContaBancaria.prox_num_conta += 1
        self.data_abertura = data_abertura if data_abertura else date.today()
        self.estado = estado
        self.tipo = tipo
        self.ordenado = ordenado
        self.taxa_juro = taxa_juro/100

    @property
    def saldo(self):
        assert self.tipo in TipoConta
        if self.tipo in (TipoConta.ORDEM, TipoConta.ORDENADO):
            return self._saldo
        else:
            if self.tipo is TipoConta.PRAZO:
                duracao_min = ContaBancaria.duracao_min_prazo
            else:
                duracao_min = ContaBancaria.duracao_min_phab

            dias = Decimal(self.duracao)
            saldo_com_juros = self._saldo * (1 + ((dias/365)*self.taxa_juro))
            return self._saldo if self.duracao < duracao_min else saldo_com_juros

    @property
    def duracao(self):
        return (date.today() - self.data_abertura).days
  
    def levantar(self, montante):
        if montante < 0:
            raise ValueError("Montante %.2f inválido!" % montante)

        if self.tipo in (TipoConta.ORDEM, TipoConta.ORDENADO):
            if self.tipo is TipoConta.ORDENADO:
                saldo_min = -self.ordenado
            else:
                saldo_min = 0

            novo_saldo = self.saldo - montante
            if novo_saldo < saldo_min:
                raise ValueError("Saldo final %.2f inferior ao saldo mínimo %.2f!"
                                 % (novo_saldo, saldo_min))

        elif self.tipo in (TipoConta.PRAZO, TipoConta.POUPANCA_HABITACAO):
            if self.tipo is TipoConta.PRAZO:
                duracao_min = ContaBancaria.duracao_min_prazo
                saldo_min = ContaBancaria.saldo_min_prazo
            else:
                duracao_min = ContaBancaria.duracao_min_phab
                saldo_min = ContaBancaria.saldo_min_phab
            
            if self.duracao < duracao_min:
                raise ValueError("Prazo mínimo %s ainda não atingido!" 
                                 % duracao_min)

            novo_saldo = self.saldo - montante
            if novo_saldo < saldo_min:
                raise ValueError("Saldo final %.2f inferior ao saldo mínimo %.2f!"
                                 % (novo_saldo, saldo_min))

            montante_sem_juros = montante / (1 + self.taxa_juro)
            novo_saldo_sem_juros = self._saldo - montante_sem_juros
            self._saldo = novo_saldo_sem_juros

        return self.saldo

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
            self.tipo.name,
            "%.2f" % self.saldo,
            self.data_abertura.strftime(DATE_FMT),
            self.estado.name,
            "%.2f" % self.ordenado,
            "%.2f" % self.taxa_juro*100,
        ))

    def __repr__(self):
        return '\n'.join((
            "ContaBancaria(",
            "    tipo=%s," % self.tipo,
            "    num_conta=%r," % self.num_conta,
            "    num_cliente=%r," % self.num_cliente,
            "    saldo=%r," % self.saldo,
            "    data_abertura=%r," % self.data_abertura,
            "    estado=%s," % self.estado,
            "    ordenado=%r," % self.ordenado,
            "    taxa_juro=%r," % (self.taxa_juro*100),
            ")"
        ))

    DATA_INICIAL = date(1997, 5, 5)
    prox_num_conta = 117
    duracao_min_prazo = int(0.25*365)
    duracao_min_phab = 18*365
    saldo_min_prazo = 100
    saldo_min_phab = 150


# CONTAS VÁLIDAS
c = ContaBancaria(
    num_cliente=1,
    saldo=Decimal('1500'),
    tipo=TipoConta.PRAZO,
    data_abertura=date(2014, 1, 5),
    taxa_juro=Decimal('2.00'),
)

contas = [
    ContaBancaria(
        num_cliente=1, 
        saldo=Decimal('100'), 
        tipo=TipoConta.ORDENADO,
        ordenado=Decimal('1680')
    ),
    ContaBancaria(
        num_cliente=2, 
        saldo=Decimal('150'),
        tipo=TipoConta.ORDENADO,
        ordenado=Decimal('750')
    ),
    ContaBancaria(
        num_cliente=1, 
        saldo=Decimal('190'),
        tipo=TipoConta.ORDEM,
    ),
    ContaBancaria(
        num_cliente=1,
        saldo=Decimal('1500'),
        tipo=TipoConta.PRAZO,
        data_abertura=date(2014, 1, 7),
        taxa_juro=Decimal('1.5'),
    ),
    ContaBancaria(
        num_cliente=3, 
        saldo=Decimal('750')        
    ),
    ContaBancaria(
        num_cliente=2, 
        saldo=Decimal('1375'),
        tipo=TipoConta.POUPANCA_HABITACAO,
        data_abertura=date(2009, 1, 7),
        taxa_juro=Decimal('2.75'),
    ),
]


def obtem_contas_cliente(num_cliente):
    return [conta for conta in contas if conta.num_cliente == num_cliente]


def patrimonio_integrado(num_cliente):
    contas_cliente = obtem_contas_cliente(num_cliente)
    if contas_cliente:
        saldo_total = 0
        print("CONTAS PARA O CLIENTE:", num_cliente, "\n")
        print("  {:^10} | {:^10} | {:^10}".format("Núm. Conta", "Tipo", "Saldo"))
        print('-'*50)
        for conta in contas_cliente:
            print("  {:10} | {:10} | {:10.2f}".format(
                conta.num_conta, 
                conta.tipo.name, 
                conta.saldo
            ))
            saldo_total += conta.saldo
        print("\n", "SALDO TOTAL: {:10.2f}".format(saldo_total))
    else:
        print("Não foram encontradas contas para o cliente com o "
              "número ", num_cliente)
