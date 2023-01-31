"""
SÉRIE DE EXERCÍCIOS 2 

Uma aplicação de chat cliente/servidor para enviar mensagens de texto 
entre dois programas, possivelmente localizados em máquinas diferentes. 
Uma mensagem pode ter várias linhas mas não pode exceder os 
140 caracteres. O utilizador deve terminar a última linha com !SEND 
para enviar a mensagem.

A aplicação de chat deverá ser invocada da seguinte forma:

$ python3 chat.py [-p PORTO]

O PORTO indicado é o porto onde a aplicação escuta pedidos de 
conversação. Por omissão tem o valor 17171.
"""

from subprocess import call
from socket import socket, AF_INET, SOCK_STREAM, SOL_SOCKET, SO_REUSEADDR


DEFAULT_SERVER_PORT = 17171
NUM_CONNECTIONS = 1
MSG_CHARS = 140


def main(local_port):
    """
    Menu inicial.
    """
    while True:
        call('clear')  # apaga ecrã... (Windows -> 'cls')
        print("ESCOLHA UMA OPÇÃO:")
        print("A. Aguardar por mensagem")
        print("E. Enviar mensagem")
        print("T. Terminar")
        opcao = input(">> ").strip().upper()

        if opcao == 'A':
            chat_server(local_port)
        elif opcao == 'E':
            chat_client()
        elif opcao == 'T':
            print("\nFim do chat\n")
            break
        else:
            print("Opção <{}> inválida".format(opcao))
            input()


def chat_client():
    """
    O cliente inicia o chat enviando uma mensagem. É ele que indica o 
    endereço e porto do servidor. Após enviar a mensagem, aguarda pela 
    resposta do servidor antes de responder novamente. Ao jeito do HTTP,
    é criado um socket por cada pedido que é fechado após a resposta.
    """
    # Solicita parâmetros do servidor ao utilizador
    server_addr = input('Endereço? [localhost] ').strip()
    if not server_addr:
        server_addr = 'localhost'
    server_port = input('Porto? [{}] '.format(DEFAULT_SERVER_PORT)).strip()
    server_port  = int(server_port) if server_port else DEFAULT_SERVER_PORT

    while True:
        # Lê mensagem introduzida pelo utilizador
        msg = input_msg()
        if not msg:
            break

        # Se houver mensagem a enviar, estabelece uma ligação 
        # envia-a e fecha o socket
        sock = socket(AF_INET, SOCK_STREAM)
        sock.connect((server_addr, server_port))
        sock.sendall(msg.encode())
        reply = sock.recv(8192)
        sock.close()

        # Mostra mensagem. Ausência de resposta é sinal para 
        # encerrar esta conversação
        if reply:
            print('>>> ', reply.decode())
        else:
            print("Ligação terminada na outra extremidade")
            break


def chat_server(local_port, bind_addr=''):
    """
    O servidor espera por uma mensagem de chat. Depois tem oportunidade
    de responder.
    """
    server_sock = socket(AF_INET, SOCK_STREAM)    
    server_sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, True)
    server_sock.bind((bind_addr, local_port))    
    server_sock.listen(NUM_CONNECTIONS)

    print("Aguardando ligações em {} {}".format(bind_addr, local_port))

    while True:
        client_sock, client_addr = server_sock.accept()
        if not chat_server_handler(client_sock):
            break    
    server_sock.close()


def chat_server_handler(client_sock):
    msg = client_sock.recv(8192)
    
    # Não havendo mensagem, fim de comunicação. Senão, mostra-a 
    # e pede resposta ao utilizador
    if msg:            
        print('>>> ', msg.decode())

        # Envia resposta se utilizador escrever algo. Msg em 
        # branco é sinal para terminar
        reply = input_msg()
        if reply:
            client_sock.sendall(msg)
        else:
            return False
    else:
        print("Ligação terminada na outra extremidade")
        return False

    client_sock.close()
    return True


def input_msg():
    """
    Lê MSG_CHARS caracteres no máximo. 
    """
    print("MSG?> ", end='')
    return input()[:140]


if __name__ == '__main__':
    from docopt import docopt
    from textwrap import dedent

    doc = r"""
    Programa para chat através de TCP.

    Usage:
    chat.py [-p PORTO]

    Options:
    -h --help     Ajuda
    -p PORTO      Porto onde aguardar ligações [default: {}]
    """.format(DEFAULT_SERVER_PORT)
    args = docopt(dedent(doc), version="Versão 1")
    main(int(args['-p']))


