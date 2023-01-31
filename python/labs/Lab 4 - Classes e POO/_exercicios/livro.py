"""
SÉRIE DE EXERCÍCIOS 4

A classe Livro desenvolvida durante o laboratório utilizada pelo 
módulo `catalogo.py`.
"""

from datetime import datetime, date


class Livro:

    def __init__(self, titulo, genero, autores, 
                 cod_isbn=None, data=None, num_exemplares=0, 
                 suporte='Capa Dura',
                 id_=None,
    ):

        if not self.titulo_valido(titulo):
            raise ValueError('Titulo %s inválido' % titulo)

        if not Livro.genero_valido(genero):
            raise ValueError('Género %s inválido' % genero)

        if not Livro.lista_autores_valida(autores):
            raise ValueError('Lista de autores %s inválida' % autores)

        if cod_isbn and not Livro.cod_isbn_valido(cod_isbn):
            raise ValueError('ISBN %s inválido' % cod_isbn)

        if not Livro.suporte_valido(suporte):
            raise ValueError('Suporte %s inválido' % suporte)


        self.titulo  = titulo
        self.genero  = genero
        self.autores = autores
        self.cod_isbn      = cod_isbn
        self.data          = data if data else date.today()  # data por omissão
        self.num_exemplares = num_exemplares
        self.suporte       = suporte
        if id_:
            self.id_ = id_
        else:
            self.id_ = Livro.prox_id
            Livro.prox_id += 1

    @classmethod
    def from_string(cls, txt):
        attrs = txt.split(',')
        return cls(
            titulo=attrs[0],
            genero=attrs[1],
            autores=[autor.strip() for autor in attrs[2].split('/') if autor],
            cod_isbn=attrs[3],
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
              self.cod_isbn if self.cod_isbn else "N/D"
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
    def cod_isbn_valido(cod_isbn):
        cod_isbn = cod_isbn.replace('-', '')
        if len(cod_isbn) < 13:
            return False
        return cod_isbn.isdigit()

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

    def __repr__(self):
        return '\n'.join((
            '%s(' % self.__class__.__name__,
            '  titulo=%r,' % self.titulo,
            '  genero=%r,' % self.genero,
            '  autores=%r,' % self.autores,
            '  cod_isbn=%r,' % self.cod_isbn, 
            '  data=%r,' % self.data, 
            '  num_exemplares=%s,' % self.num_exemplares,
            '  suporte=%r,' % self.suporte,
            ')'
        ))

    prox_id = 1


# liv1 = Livro(
#     titulo='Programming C# 5.0', 
#     genero='Informática', 
#     autores=['Ian Griffiths'],
#     cod_isbn='978-1449320416',
#     data=date(2012, 10, 31),
#     num_exemplares=20,
#     suporte='Capa Mole'
# )


# liv2 = Livro(
#     titulo='The C++ Programming Language, 4th Edition', 
#     genero='Informática', 
#     autores=['Bjarne Stroustrup'],
#     cod_isbn='978-0321563842',   
#     data=date(2013, 5, 19),
#     num_exemplares=17,
#     suporte='Capa Mole'
# )

# liv3 = Livro(
#     titulo="Manual Tipográfico", 
#     genero="Tipografia", 
#     autores=['N/D']
# )

# txt = 'Starting Out With Python 2nd Ed.,Informática,'
#       'Tony Gaddis/,978-0-13-257637-6,2012-10-31,20,Capa Mole'
# liv4 = Livro.from_string(txt)
