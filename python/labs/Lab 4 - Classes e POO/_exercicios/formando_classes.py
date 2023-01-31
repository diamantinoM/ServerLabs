from datetime import date, datetime
from typing import Tuple, List, Union


class Formando:

    def __init__(
            self, 
            nome: str, 
            data_nascimento: Tuple[int], 
            morada: str, 
            modulos_tecnicos: List[str], 
            modulos_gerais: List[str]
    ):
        if len(nome) < 2:
            raise ValueError("Nome completo com menos de dois nomes")

        self.nome = nome
        self._data_nascimento = int(datetime(*data_nascimento).timestamp())
        # self.data_nascimento = date(*data_nascimento)
        self.morada = morada
        self.modulos_tecnicos = modulos_tecnicos
        self.modulos_gerais = modulos_gerais

    @property
    def apelidos(self):
        return ' '.join(self.nome.split()[1:])

    @property
    def modulos_inscritos(self):
        return self.modulos_tecnicos + self.modulos_gerais

    def __str__(self):
        return f'Formando: {self.nome}, {self.data_nascimento}'


form1 = Formando(
    nome='Alberto Silva', 
    data_nascimento=(1994, 10, 27),
    morada='Praça da Alegria, Lisboa',
    modulos_tecnicos=['Linux', 'C++', 'Windows Server'],
    modulos_gerais=['Inglês', 'Português'],
)

form2 = Formando(
    nome='Alberto Alves Almeida',
    data_nascimento=(2015, 10, 20),
    morada='Av. Liberdade N. 13 Lisboa', 
    modulos_tecnicos=['Linux', 'SQL', 'Windows Server'],
    modulos_gerais=['Inglês', 'Português'],
)

print(form1.nome)
print(form1.data_nascimento)
print(form1.data_nascimento.year)
form1.data_nascimento = date(1974, 10, 27)
form1.data_nascimento = (1974, 10, 27)





