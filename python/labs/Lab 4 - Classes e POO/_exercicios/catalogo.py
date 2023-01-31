"""
SÉRIE DE EXERCÍCIOS 4

Pretende implementar um catálogo de livros. Para tal, desenvolva uma
classe (eg, Catalogo ou ListaLivros) especializada em gerir uma lista 
de livros. [etc...consultar restante enunciado]
"""

from datetime import date
from livro import Livro


class Catalogo:

    def __init__(self, livros=None):
        if livros:
            for liv in livros:
                self._verifica_livro_sem_repeticao(liv)
            self._catalogo = livros
        else:
            self._catalogo = []


    def adiciona_livro(self, liv):
        self._verifica_livro_sem_repeticao(liv)        
        self._catalogo.append(liv)


    def obtem_por_id(self, id_):
        encontrados = (liv for liv in self._catalogo if liv.id_ == id_)
        try:
            return next(encontrados)
        except StopIteration:
            return None


    def remove_por_id(self, id_):
        for i, liv in enumerate(self._catalogo):
            if liv.id_ == id_:
                return self._catalogo.pop(i)
        raise ValueError('ID %s não está no catalogo' % id_)


    def __contains__(self, liv):
        return bool(self.obtem_por_id(liv.id_))


    def __len__(self):
        return len(self._catalogo)


    def __getitem__(self, index):
        return self._catalogo[index]


    def _verifica_livro_sem_repeticao(self, liv):
        self._verificaLivro(liv)
        if self.obtem_por_id(liv.id_):
            raise LivroDuplicado('Já existe um livro com id %s em catálogo' % liv.id_)


    @staticmethod
    def _verificaLivro(item):
        if not isinstance(item, Livro):
            raise TypeError('Item %s deve ser do tipo %s' % (item, Livro))


class LivroDuplicado(Exception):
    pass

# Testes

if __name__ == '__main__':
    liv1 = Livro(
        titulo='Programming C# 5.0', 
        genero='Informática', 
        autores=['Ian Griffiths'],
        cod_isbn='978-1449320416',
        data=date(2012, 10, 31),
        num_exemplares=20,
        suporte='Capa Mole'
    )

    liv2 = Livro(
        titulo='The C++ Programming Language, 4th Edition', 
        genero='Informática', 
        autores=['Bjarne Stroustrup'],
        cod_isbn='978-0321563842',   
        data=date(2013, 5, 19),
        num_exemplares=17,
        suporte='Capa Mole'
    )

    liv3 = Livro(
        titulo="Manual Tipográfico", 
        genero="Tipografia", 
        autores=['N/D']
    )


    txt = \
        'Starting Out With Python 2nd Ed.,Informática,' \
        'Tony Gaddis/,978-0-13-257637-6,2012-10-31,20,Capa Mole'
    liv4 = Livro.from_string(txt)

    catal = Catalogo()
    catal.adiciona_livro(liv1)
    catal.adiciona_livro(liv2)

    try:
        catal.adiciona_livro(liv1)
    except LivroDuplicado:
        print("Livro já existente")


    print("liv1 in catal", liv1 in catal)
    print("liv4 in catal", liv4 in catal)
    print(len(catal))

    it = iter(catal)
    print(next(it))