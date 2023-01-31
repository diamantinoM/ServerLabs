"""
SÉRIE DE EXERCÍCIOS 4

Exercícios de revisão sobre herança.
"""

from decimal import Decimal


class Colaborador:

    def __init__(self, sal_base):
        self.sal_base = sal_base

    def vencimento(self):
        return self.sal_base + self.obtemBonus()

    def obtemBonus(self):
        return 50


class ColaboradorSenior(Colaborador):

    # Construtor desnecessário
    # def __init__(self, sal_base):
    #     super().__init__(sal_base)


    def obtemBonus(self):
        return super().obtemBonus() + 200
        #return 200


def teste1():
    c = Colaborador(Decimal('1000'))
    print(c.vencimento())
            
    c = ColaboradorSenior(Decimal('1000'))
    print(c.vencimento())

#teste1()


class Pessoa:

    def __init__(self, nome):
        self.nome = nome        

    def apresenteSe(self):
        return "Eu sou o/a " + self.nome + "."


class PessoaFormal(Pessoa):

    def __init__(self, nome, titulo):
        super().__init__(nome)
        self.titulo = titulo

    def apresenteSe(self):
        return super().apresenteSe() + " Ao seu dispor."
    
    def obtemTitulo(self):
        return self.titulo


def teste2():    
    p = Pessoa("Alberto")
    print(p.apresenteSe())

    p = PessoaFormal("Armando", "Doutor")
    print(p.apresenteSe())

    