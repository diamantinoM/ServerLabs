# 1. Euros -> Dólares
# 2. Dólares -> Euros
# T. Terminar o programa
# > 1
# Montante em Euros: 1000
# Dólares -> 1100
# 1. Euros -> Dólares
# 2. Dólares -> Euros
# T. Terminar o programa
# > 1

from decimal import Decimal as dec

def main():
    while True:
        cambio_eur_usd = dec('1.1')

        # 1. Exibir o menu
        print("1. Euros -> Dólares")
        print("2. Dólares -> Euros")
        print("3. Euros -> Libras Esterlinas")
        print("E. Encerrar o programa")

        # 2. Ler opção
        opcao = input("> ")

        # 3. Analisar e executar a opção
        if opcao == '1':
            montante = dec(input("Montante em Euros: "))
            print(f"Dólares -> {montante * cambio_eur_usd:.2f}")
        elif opcao == '2':
            montante = dec(input("Montante em Dólares: "))
            print(f"Euros -> {montante / cambio_eur_usd:.2f}")
        elif opcao == '3':
            print(f"Opção ainda não implementada")
        elif opcao.upper() == 'T':
            print("Programa vai terminar")
            break
        #:
    #:
#:

if __name__ == '__main__':
    main()
#:

# int, float, bool, str -> tipos primitivos da linguagem