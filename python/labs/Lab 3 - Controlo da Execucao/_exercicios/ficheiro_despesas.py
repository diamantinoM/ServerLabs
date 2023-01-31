"""
SÉRIE DE EXERCÍCIOS 3 - Controlo da Execução

Altere os primeiros dois exemplos do laboratório 3 (mostraDespesas 1 
e 2) de modo a não terminar logo assim que encontra uma linha errada. 
Ou seja, apenas alerta para o erro e depois prossegue para a p
próxima linha.
"""

from datetime import datetime
from decimal import Decimal, DecimalException


def mostraDespesas1(nome_fich):
    fich = None
    try:
        fich = open(nome_fich, 'r')
        for linha in fich:
            if linha.isspace():
                continue
            if linha.strip()[0] == '#':
                continue

            try:
                despesa = linha.split(',')
                desc = despesa[0].strip()
                data = datetime.strptime(despesa[1].strip(), '%d-%m-%Y').date()
                montante = Decimal(despesa[2])
                print("{:30} {} {:15.2f}".format(desc, data, montante))
            except (ValueError, DecimalException, IndexError) as ex:
                print("[-] ATENÇÃO: Linha inválida ->", linha, end='')
                print("    ERRO:", ex)
    except Exception as ex:
        print("ATENÇÃO: Ocorreu um erro!\n", ex)
    finally:
        if fich:    
            fich.close()


def mostraDespesas2(nome_fich):
    with open(nome_fich, 'r') as fich:
        try:
            for linha in fich: 
                if linha.isspace():
                    continue
                if linha.strip()[0] == '#':
                    continue
                try:
                    despesa = linha.split(',')
                    desc = despesa[0].strip()
                    data = datetime.strptime(despesa[1].strip(), '%d-%m-%Y').date()
                    montante = Decimal(despesa[2])
                    print("{:30} {} {:15.2f}".format(desc, data, montante))
                except (ValueError, DecimalException, IndexError) as ex:
                    print("[-] ATENÇÃO: Linha inválida ->", linha, end='')
                    print("    ERRO:", ex)
        except Exception as ex:
            print("ATENÇÃO: Ocorreu um erro!\n", ex)


def linhasRelevantes(iteravel):
    for linha in iteravel:
        if linha.isspace():
            continue
        if linha.strip()[0] == '#':
            continue
        yield linha


def mostraDespesas3(nome_fich):
    linhas_invalidas = []
    with open(nome_fich, 'r') as fich:
        try:
            for linha in linhasRelevantes(fich):
                try:
                    despesa = linha.split(',')
                    desc = despesa[0].strip()
                    data = datetime.strptime(despesa[1].strip(), '%d-%m-%Y').date()
                    montante = Decimal(despesa[2])
                    print("{:30} {} {:15.2f}".format(desc, data, montante))
                except (ValueError, DecimalException, IndexError) as ex:
                    linhas_invalidas.append(linha)
        except Exception as ex:
            print("ATENÇÃO: Ocorreu um erro!\n", ex)

    if linhas_invalidas:
        print("\nForam encontradas %s linhas inválidas:" % len(linhas_invalidas))
        print('', *linhas_invalidas, sep='  ')


if __name__ == '__main__':
    mostraDespesas3('ficheiro_despesas.txt')


