from datetime import date

class Formando:
    def __init__(self, nome, data_nascimento, morada, modulos_tecnicos, modulos_gerais):
        if len(nome) < 2 or nome.isdigit():
            raise ValueError(f'Nome inválido {nome}')
        self.nome = nome
        # self.prim_nome = nome.split()[0]
        # self.apelidos = ' '.join(nome.split()[1:])

        # self.data_nascimento = int(datetime(*data_nascimento).timestamp())
        self.data_nascimento = data_nascimento
        self.morada = morada
        self.modulos_tecnicos = modulos_tecnicos
        self.modulos_gerais = modulos_gerais
    #:
    @property
    def apelidos(self):
        return ' '.join(self.nome.split()[1:])
    #:
    @property
    def modulos_inscritos(self):
        return self.modulos_tecnicos + self.modulos_gerais
    #:
    @property
    def ano(self):
        return self.data_nascimento.year
    #:
    def __str__(self):
        return f'Formando: {self.nome}, {self.data_nascimento}'
    #:
#:

form1 = Formando(
    nome='Alberto Silva', 
    data_nascimento=date(1994, 10, 27),
    morada='Praça da Alegria, Lisboa',
    modulos_tecnicos=['Linux', 'C++', 'Windows Server'],
    modulos_gerais=['Inglês', 'Português'],
)

form2 = Formando(
    nome='Alberto Alves Almeida',
    data_nascimento=date(2015, 10, 20),
    morada='Av. Liberdade N. 13 Lisboa', 
    modulos_tecnicos=['Linux', 'SQL', 'Windows Server'],
    modulos_gerais=['Inglês', 'Português'],
)

print(form1.nome)
print(form1.data_nascimento)
print(form1.ano)
form1.data_nascimento = date(1974, 10, 27)
# form1.data_nascimento = (1974, 10, 27)
print(form1)

