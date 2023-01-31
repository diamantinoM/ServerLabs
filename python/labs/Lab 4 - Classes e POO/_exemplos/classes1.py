"""
LABORATÓRIO 4 - Classes e Programação Orientada por Objectos

Representação em memória de uma BD para lidar com livros.
""" 

from datetime import datetime, date


class Livro:

    def __init__(self, titulo, genero, autores, 
                 cod_ISBN=None, data=None, num_exemplares=0, 
                 suporte='Capa Dura'):

        if not self.titulo_valido(titulo):
            raise ValueError('Titulo %s inválido' % titulo)

        if not Livro.genero_valido(genero):
            raise ValueError('Género %s inválido' % genero)

        if not Livro.lista_autores_valida(autores):
            raise ValueError('Lista de autores %s inválida' % autores)

        if cod_ISBN and not Livro.cod_isbn_valido(cod_ISBN):
            raise ValueError('ISBN %s inválido' % cod_ISBN)

        if not Livro.suporte_valido(suporte):
            raise ValueError('Suporte %s inválido' % suporte)

        self.titulo  = titulo
        self.genero  = genero
        self.autores = autores
        self.cod_ISBN      = cod_ISBN
        self.data          = data if data else date.today() # data por omissão
        self.num_exemplares = num_exemplares
        self.suporte       = suporte

    @classmethod
    def from_string(cls, txt):
        attrs = txt.split(',')
        return cls(
            titulo=attrs[0],
            genero=attrs[1],
            autores=[autor.strip() for autor in attrs[2].split('/') if autor],
            cod_ISBN=attrs[3],
            data=datetime.strptime(attrs[4].strip(), '%Y-%m-%d').date(),
            num_exemplares=int(attrs[5]),
            suporte=attrs[6],
        )

    def __str__(self):
        return "{}: {} {}".format(self.titulo,  ','.join(self.autores), self.data)

    def mostra(self):
        print('-' * 80)
        print("LIVRO: ", self.titulo)
        print('-' * 80)
        print("{:<25}: {}".format(
            "Código ISBN", 
            self.cod_ISBN if self.cod_ISBN else "N/D"
        ))
        print("{:<25}: {}".format("Género", self.genero))

        legenda = "Autores"
        for autor in self.autores:
            print("{:<25}: {}".format(legenda, autor))
            legenda = ""
        
        print("{:<25}: {}".format("Data", self.data))
        print("{:<25}: {}".format("Número de Exemplares", self.num_exemplares))
        print("{:<25}: {}".format("Suporte", self.suporte))


    @staticmethod  
    def cod_isbn_valido(cod_ISBN):
        cod_ISBN = cod_ISBN.replace('-', '')
        if len(cod_ISBN) < 13:
            return False
        return cod_ISBN.isdigit()

    @staticmethod  
    def titulo_valido(titulo):
        return bool(titulo)

    @staticmethod
    def genero_valido(genero):
        if not genero:
            return False
        return genero in {
            'Arte',
            'Biologia', 
            'Ciências',
            'Economia',
            'Informática',
            'Literatura',
            'Matemática',
            'Tipografia',
        }

    @staticmethod  
    def lista_autores_valida(autores):
        if not autores:
            return False
        return [autor for autor in autores if autor]

    @staticmethod  
    def suporte_valido(suporte):
        if not suporte:
            return False
        return suporte in {
            'Capa Dura',
            'Capa Mole',
            'eBook',
        }

    @property
    def ano(self):
        return self.data.year


liv1 = Livro(
    titulo='Programming C# 5.0', 
    genero='Informática', 
    autores=['Ian Griffiths'],
    cod_ISBN='978-1449320416',
    data=date(2012, 10, 31),
    num_exemplares=20,
    suporte='Capa Mole'
)

liv2 = Livro(
    titulo='The C++ Programming Language, 4th Edition', 
    genero='Informática', 
    autores=['Bjarne Stroustrup'],
    cod_ISBN='978-0321563842',   
    data =date(2013, 5, 19),
    num_exemplares = 17,
    suporte = 'Capa Mole'
)

liv3 = Livro(
    titulo="Manual Tipográfico", 
    genero="Tipografia", 
    autores=['N/D']
)

txt = 'Starting Out With Python 2nd Ed.,Informática,Tony Gaddis/,978-0-13-257637-6,2012-10-31,20,Capa Mole'
liv4 = Livro.from_string(txt)

print(liv3.ano)

# class Livro:
#     def __init__(self, titulo, genero, autores):
#         self.titulo  = titulo
#         self.genero  = genero
#         self.autores = autores

#         self.cod_ISBN       = None
#         self.data          = date.today()  # data por omissão
#         self.num_exemplares = 0
#         self.suporte       = 'Capa Dura'

#     def __str__(self):
#        return "{}: {} {}".format(self.titulo,  ','.join(self.autores), self.data)

# liv1 = Livro('Programming C# 5.0', 'Informática', ['Ian Griffiths'])
# liv1.cod_ISBN = '978-1449320416'
# liv1.data = date(2012, 10, 31)
# liv1.num_exemplares = 20
# liv1.suporte = 'Capa Mole'


# liv2 = Livro('The C++ Programming Language, 4th Edition', 'Informática',
#              ['Bjarne Stroustrup'])
# liv2.codISBN = '978-0321563842'
# liv2.data = date(2013, 5, 19)
# liv2.num_exemplares = 17
# liv2.suporte = 'Capa Mole'


# class Livro:
#     def __init__(self):
#        self.cod_ISBN = None
#        self.titulo = 'N/D'
#        self.genero = 'N/D'
#        self.autores = []
#        self.data = None
#        self.num_exemplares = -1
#        self.suport = 'N/D'

#     def __str__(self):
#        return "{}: {} {}".format(self.titulo,  ','.join(self.autores), self.data)

# liv2 = Livro()
# liv1.cod_ISBN = '978-1449320416'
# liv1.titulo = 'Programming C# 5.0'
# liv1.genero = 'Informática'
# liv1.autores = ['Ian Griffiths']
# liv1.data = date(2012, 10, 31)
# liv1.num_exemplares = 20
# liv1.suporte = 'Capa Mole'


# liv2 = Livro()
# liv2.codISBN = '978-0321563842'
# liv2.titulo = 'The C++ Programming Language, 4th Edition'
# liv2.genero = 'Informática'
# liv2.autores = ['Bjarne Stroustrup']
# liv2.data = date(2013, 5, 19)
# liv2.num_exemplares = 17
# liv2.suporte = 'Capa Mole'


# class Pessoa:

#     def __init__(self, nome_completo, data_nascimento):
#         self.nome_completo = nome_completo
#         self._data_nascimento = data_nascimento

#     @property
#     def apelido(self):
#         return self.nome_completo.rpartition(' ')[-1]

#     @apelido.setter
#     def apelido(self, novo_apelido):
#         self.nome_completo += (' ' + novo_apelido)


#     def setApelido(self, novo_apelido):


# class Circunferencia:
#     def __init__(self, raio):
#         self.diametro = 2*raio

#     @property
#     def raio(self):
#         return self.diametro / 2

#     # ...

# c = Circunferencia(2)
# print(c.raio)
# print(c.raio * 3)
