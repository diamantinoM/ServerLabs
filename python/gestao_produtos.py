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


    @classmethod
    def from_csv(cls, linha: str, delim = CSV_DEFAULT_DELIM) -> 'Produto':
        attrs = linha.split(delim)
        return cls(
            id_ = int(attrs[0]),
            nome = attrs[1],
            tipo = attrs[2],
            quantidade = int(attrs[3]),
            preco = dec(attrs[4]),
        )


    @property
    def desc_tipo(self) -> str:
        return PRODUCT_TYPES[self.tipo]


    def __str__(self) -> str:
        cls_name = self.__class__.__name__
        return f'{cls_name}[id_ = {self.id_}  nome = "{self.nome}" tipo = "{self.tipo}"]'

    def __repr__(self) -> str:
        cls_name = self.__class__.__name__
        return f'{cls_name}(id_ ={self.id_}, nome={self.nome}, tipo={self.tipo}, quantidade={self.quantidade}, preco={repr(self.preco)})'

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


###################################################################################
##
##          LEITURA DE FICHEIROS
##
###################################################################################

def le_produtos(caminho_fich: str, delim = CSV_DEFAULT_DELIM) -> CatalogoProdutos:
    prods = CatalogoProdutos()
    # ler ficheiro e popular catalogo com cada um dos produtos
    # uma linha do ficheiro corresponde a um produto
    with open(caminho_fich, 'rt') as fich:
        for linha in linhas_relevantes(fich):
            prods.append(Produto.from_csv(linha, delim))
    return prods


def linhas_relevantes(fich: TextIO):
    for linha in fich:
        linha = linha.strip()
        if len(linha) == 0 or linha[0] == '#':
            continue
        yield linha


##################################################################################
##
##       MENU, OPÇÕES E INTERACÇÃO COM UTILIZADOR
##
##################################################################################


def exibe_msg(*args, ident = DEFAULT_INDENTATION, **kargs):
    print(' ' * (ident - 1), *args, **kargs)


def entrada(msg: str, ident = DEFAULT_INDENTATION):
    return input(f"{' ' * DEFAULT_INDENTATION}{msg}")


def cls():
    if sys.platform == 'win32':
        subprocess.run(['cls'], shell=True, check=True)
    elif sys.platform in ('darwin', 'linux', 'bsd', 'unix'):
        subprocess.run(['clear'], check=True)


def pause(msg: str="Pressione ENTER para continuar...", ident = DEFAULT_INDENTATION):
    input(f"{' ' * ident}{msg}")


produtos : CatalogoProdutos | None = None


def exec_menu():
    """
    - Lista o catálogo 
    - Pesquisar por alguns campos
    - Eliminar um registo do catálogo
    - Guardar o catálogo em ficheiro
    """

    while True:
        cls()
        exibe_msg("*******************************************")
        exibe_msg("* L - Listar catálogo                     *")
        exibe_msg("* P - Pesquisar por id                    *")
        exibe_msg("* A - Acrescentar produto                 *")
        exibe_msg("* E - Eliminar produto                    *")
        exibe_msg("* G - Guardar catálogo em ficheiro        *")
        exibe_msg("*                                         *")
        exibe_msg("* T - Terminar programa                   *")
        exibe_msg("*******************************************")

        print()
        opcao = entrada("OPCAO> ").strip().upper()

        if opcao in ('L', 'LISTAR'):
            exec_listar()
        elif opcao in ('T', 'TERMINAR'):
            break
            exec_terminar()
        else:
            exibe_msg(f"Opção {opcao} inválida!")
            pause()


def exec_listar():
    cabecalho = f'{"ID":^8}|{"Nome":^26}|{"Tipo":^8}|{"Quantidade":^16}|{"Preço":^16}'
    separador = f'{"-" * 8}+{"-" * 26}+{"-" * 8}+{"-" * 16}+{"-" * 16}'
    # separador =  '|'.join(['-' * 16] * 5)
    print()
    exibe_msg(cabecalho)
    exibe_msg(separador)
    for prod in produtos:
        linha = f'{prod.id_:^8}|{prod.nome:^26}|{prod.tipo:^8}|{prod.quantidade:^16}|{prod.preco:^16}'
        exibe_msg(linha)
    
    exibe_msg(separador)
    print()
    pause()


def exec_terminar():
    sys.exit(0)



def main() -> None:
    global produtos
    produtos = le_produtos('produtos.csv')
    exec_menu()


if __name__ == '__main__':
    main()