"""
Programa para gestão do catálogo de produtos. Este programa permite:
    - Lista o catálogo
    - Pesquisar por alguns campos
    - Eliminar um registo do catálogo
    - Guardar o catálogo dem ficheiro
"""

from decimal import Decimal as dec
import subprocess
import sys
from typing import TextIO

CSV_DEFAULT_DELIM = ','
DEFAULT_INDENTATION = 3

###################################################################################
##
##      PRODUTOS E CATÁLOGO
##
###################################################################################

PRODUCT_TYPES = {
    'AL': 'Alimentação',
    'DL': 'Detergente p/ Loiça',
    'FRL': 'Frutas e Legumes'
}

# id         : > 0 e tem que ter 5 digitos
# tipo
# nome
# preco
# quantidade

class Produto:
    def __init__(
        self, 
        id_: int, 
        nome: str,
        tipo: str,
        quantidade: int, 
        preco: dec
    ):
        if id_ < 0 or len(str(id_)) != 5:
            raise InvalidProdAttribute(f'{id_=} inválido (deve ser > 0 e ter 5 dígitos)')

        if not nome:
            raise InvalidProdAttribute('Nome vazio')

        if tipo not in PRODUCT_TYPES:
            raise InvalidProdAttribute(f'Tipo de produto ({tipo}) desconhecido')

        if quantidade < 0:
            raise InvalidProdAttribute('Quantidade deve ser >= 0')

        if preco < 0:
            raise InvalidProdAttribute('Preço deve ser >= 0')

        self.id_ = id_
        self.nome = nome
        self.tipo = tipo
        self.quantidade = quantidade
        self.preco = preco


    @property
    def desc_tipo(self) -> str:
        return PRODUCT_TYPES[self.tipo]


    def __str__(self) -> str:
        cls_name = self.__class__.__name__
        return f'{cls_name}[id_={self.id_}  nome= "{self.nome}" tipo = "{self.tipo}"]'

    def __repr__(self) -> str:
        cls_name = self.__class__.__name__
        return f'{cls_name}(id_={self.id_}, nome={self.nome}, tipo={self.tipo}, quantidade={self.quantidade}, preco={repr(self.preco)})'

    def com_iva(self, taxa_iva: dec) -> dec:
        return self.preco * (1 + taxa_iva/100)



class InvalidProdAttribute(ValueError):
    pass



class CatalogoProdutos:
    def __init__(self):
        self._prods = {}


    def append(self, prod: Produto):
        if prod.id_ in self._prods:
            raise DuplicateValue(f'Já existe produto com id {prod.id_} no catálogo')
        self._prods[prod.id_] = prod


    def _dump(self):
        for prod in self._prods.values():
            print(prod)


    def obtem_por_id(self, id: int) -> Produto | None:
        return self._prods.get(id)


    def pesquisa(self, criterio) -> 'CatalogoProdutos':
        encontrados = CatalogoProdutos()
        for prod in self._prods.values():
            if criterio(prod):
                encontrados.append(prod)
        return encontrados


    def __str__(self):
        class_name = self.__class__.__name__
        return f'{class_name}[#produtos = {len(self._prods)}]'


    def __iter__(self):
        for prod in self._prods.values():
            yield prod


    def __len__(self):
        return len(self._prods)



class DuplicateValue(Exception):
    pass


def main() -> None:
    produtos = CatalogoProdutos()
    produtos.append(Produto(30987, 'pão de milho', 'AL', 2, dec('1')))
    produtos.append(Produto(30098, 'leite mimosa', 'AL', 10, dec('2')))
    produtos.append(Produto(21109, 'fairy', 'DL', 20, dec('3')))
    # produtos.append(Produto(21109, 'fairy', 'DL', 20, dec('3')))
    
    produtos._dump()


if __name__ == '__main__':
    main()