import datetime
import subprocess
import sys
from typing import TextIO

CSV_DEFAULT_DELIM = '//'
DEFAULT_INDENTATION = 3

###################################################################################
##
##      VIATURA E CATÁLOGO
##
###################################################################################

class Viatura:
    def __init__(self, matricula: str, marca: str, modelo: str, data: datetime):

        #TODO IF'S


        self.matricula = matricula
        self.marca = marca
        self.modelo = modelo
        self.data = data

    @classmethod
    def from_csv(cls, linha: str, delim = CSV_DEFAULT_DELIM) -> 'Viatura':
        attrs = linha.split(delim)
        return cls(
            matricula = attrs[0],
            marca = attrs[1],
            modelo = attrs[2],
            data = datetime.datetime.strptime(attrs[3], '%Y-%m-%d').date()
    )

    def __str__(self):
        return f"{self.matricula} {self.marca} {self.modelo} {self.data}"


    def __repr__(self) -> str:
        cls_name = self.__class__.__name__
        return f'{cls_name}(matricula={self.matricula}, marca={self.marca}, modelo={self.modelo}, data={self.data})'


class InvalidProdAttribute(ValueError):
    pass


class CatalogoViaturas:
    def __init__(self):
        self._viatura = {}


    def append(self, viatura: Viatura):
        if viatura.matricula in self._viatura:
            raise DuplicateValue(f'Já existe veículo com matrícula {viatura.matricula} no catálogo')
        self._viatura[viatura.matricula] = viatura

    def _dump(self):
        for viatura in self._viatura.values():
            print(viatura)

    def obtem_por_matricula(self, matricula: str) -> Viatura | None:
        return self._viatura.get(matricula)

    def pesquisa(self, criterio) ->  'CatalogoViaturas':
        encontrados = CatalogoViaturas()
        for viatura in self._viatura.values():
            if criterio(viatura):
                encontrados.append(viatura)
        return encontrados

    def __str__(self):
        class_name = self.__class__.__name__
        return f'{class_name}[#veículos = {len(self._viatura)}]'

    def __iter__(self):
        for viatura in self._viatura.values():
            yield viatura

    def __len__(self):
        return len(self._viatura)


class DuplicateValue(Exception):
    pass


###################################################################################
##
##          LEITURA DE FICHEIROS
##
###################################################################################

def le_viatura(caminho_fich: str, delim = CSV_DEFAULT_DELIM) -> CatalogoViaturas:
    viaturas = CatalogoViaturas()
    # ler ficheiro e popular catalogo com cada viatura
    # uma linha do ficheiro corresponde a um viatura
    with open(caminho_fich, 'rt') as fich:
        for linha in linhas_relevantes(fich):
            viaturas.append(Viatura.from_csv(linha, delim))
    return viaturas

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


viaturas : CatalogoViaturas | None = None


def exec_menu():

    while True:
        cls()
        exibe_msg("*******************************************")
        exibe_msg("* 1 - Listar Viaturas                     *")
        exibe_msg("* 2 - Pesquisar Viaturas                  *")
        exibe_msg("* 3 - Adicionar Viatura                   *")
        exibe_msg("* 4 - Remover Viatura                     *")
        exibe_msg("* 5 - Atualizar Catálogo                  *")
        exibe_msg("* 6 - Recarregar Catálogo                 *")
        exibe_msg("*                                         *")
        exibe_msg("* T - Terminar programa                   *")
        exibe_msg("*******************************************")

        print()
        opcao = entrada("OPCAO >> ").strip().upper()

        if opcao in ('1', 'UM'):
            exec_listar()
        elif opcao in ('T', 'TERMINAR'):
            break
            exec_terminar()
        else:
            exibe_msg(f"Opção {opcao} inválida!")
            pause()

#TODO all the menu options

def exec_listar():
    cabecalho = f'{"Matrícula":^16}|{"Marca":^20}|{"Modelo":^20}|{"Data":^16}'
    separador = f'{"-" * 16}+{"-" * 20}+{"-" * 20}+{"-" * 16}'
    print()
    exibe_msg(cabecalho)
    exibe_msg(separador)
    for viatura in viaturas:
        linha = f'{viatura.matricula:^16}|{viatura.marca:^20}|{viatura.modelo:^20}|{viatura.data.strftime("%Y-%m-%d"):^16}'
        exibe_msg(linha)

    exibe_msg(separador)
    print()
    pause()


def exec_terminar():
    sys.exit(0)



def main() -> None:
    global viaturas
    viaturas = le_viatura('viaturas.csv')
    exec_menu()


if __name__ == '__main__':
    main()