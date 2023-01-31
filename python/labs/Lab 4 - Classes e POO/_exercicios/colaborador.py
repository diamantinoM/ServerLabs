"""
SÉRIE DE EXERCÍCIOS 4

Uma aplicação de gestão necessita de lidar com informação sobre os 
seus colaboradores [etc...consultar restante enunciado].
"""

from decimal import Decimal as dec


taxa_irs = dec('0.15')
tsu = dec('0.11')


class Colaborador:

    def __init__(
            self, 
            prim_nome, 
            apelido, 
            salario_anual,
            num_meses_venc
    ):
        if len(prim_nome) < 2:
            raise ValueError("Nome %s inválido" % prim_nome)
        if len(apelido) < 2:
            raise ValueError("Apelido %s inválido" % apelido)
        if salario_anual < 0:
            raise ValueError("Salario anual %s inválido" % salario_anual)
        if num_meses_venc not in (12, 14):
            raise ValueError(
                "Número de meses de vencimento %s inválido", 
                num_meses_venc
            )

        self.prim_nome = prim_nome
        self.apelido = apelido
        self.salario_anual = salario_anual
        self.num_meses_venc = num_meses_venc

    @property
    def nome_completo(self):
        return self.prim_nome + ' ' + self.apelido

    @property
    def salario_anual_liq(self):
        return self.salario_anual * (1 - taxa_irs - tsu)

    @property
    def salario_mensal_liq(self):
        return self.salario_anual_liq/self.num_meses_venc

    def __str__(self):
        return f'{self.prim_nome},{self.apelido},{self.salario_anual},{self.num_meses_venc}'

    def __repr__(self):
        return '\n'.join((
            '%s(' % self.__class__.__name__,
            " prim_nome='%s'," % self.prim_nome,
            " apelido='%s'," % self.apelido,
            ' salario_anual=%r,' % self.salario_anual,
            ' num_meses_venc=%r,' % self.num_meses_venc,
            ')'
        ))

c = Colaborador(
    prim_nome='Alberto',
    apelido='Antunes',
    salario_anual=dec('14400.00'),
    num_meses_venc=12,
)

print(c.salario_mensal_liq)
