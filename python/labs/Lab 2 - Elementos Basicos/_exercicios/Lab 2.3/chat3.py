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

NOTA: Esta versão está organizada em funções e reutiliza sempre o 
mesmo socket cliente para evitar múltiplos pedidos de ligação. 
Contínua síncrono (uma mensagem enviada à vez por cada um dos pares da
conversação), mas as mensagens agora têm dimensão fixa.
"""

from subprocess import call
from socket import socket, AF_INET, SOCK_STREAM, SOL_SOCKET, SO_REUSEADDR
from textwrap import fill


DEFAULT_SERVER_PORT = 17171
NUM_CONNECTIONS = 3
MSG_CHARS = 140
MSG_LEN = MSG_CHARS * 2
PADDING = b'\x00'
SEND_CMD = '!!s'
END_CMD = '!!e'


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
    resposta do servidor antes de responder novamente.
    """
    # Solicita parâmetros do servidor ao utilizador
    server_addr = input('Endereço? [localhost] ').strip()
    if not server_addr:
        server_addr = 'localhost'
    server_port = input('Porto? [{}] '.format(DEFAULT_SERVER_PORT)).strip()
    server_port  = int(server_port) if server_port else DEFAULT_SERVER_PORT

    # Estabelece ligação ao servidor
    print(server_addr, server_port)
    client_sock = socket(AF_INET, SOCK_STREAM)
    client_sock.connect((server_addr, server_port))

    # Ciclo do cliente: envia mensagens enquanto utilizador não terminar 
    # conversação (END_CMD) ou enquanto o servidor não fechar o socket
    while True: 
        if read_and_send_msg(client_sock) == END_CMD:
            break

        if not recv_and_show_msg(client_sock):
            print("Ligação fechada na outra extremidade!")
            break
              
    client_sock.close()


def chat_server(local_port, bind_addr=''):
    """
    O servidor espera por uma mensagem de chat. Depois tem oportunidade
    de responder.
    """
    server_sock = socket(AF_INET, SOCK_STREAM)    
    server_sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, True)
    server_sock.bind((bind_addr, local_port))    
    server_sock.listen(NUM_CONNECTIONS)

    client_sock, client_addr = server_sock.accept()
    print("Ligação estabelecida com {}".format(client_addr))

    # Ciclo do servidor: semelhante ao do cliente, mas ao contrário
    while True:
        if not recv_and_show_msg(client_sock):
            print("Ligação fechada na outra extremidade!")
            break

        if read_and_send_msg(client_sock) == END_CMD:
            break

    client_sock.close()
    server_sock.close()

   
def read_and_send_msg(client_sock):
    """
    Pequena função que pode ser reutilizada pelo cliente e pelo 
    servidor. Pede ao utilizador uma msg e tenta enviá-la.  
    Devolve comando introduzido pelo utilizador.
    """
    msg, cmd = input_msg()
    if msg:
        send_chat_msg(client_sock, msg)
    return cmd


def recv_and_show_msg(client_sock):
    """
    Pequena função que pode ser reutilizada pelo cliente e pelo 
    servidor. Aguarda por uma mensagem remota a e mostra-a ao 
    utilizador. Devolve False se a mensagem veio vazia, sinal de que a
    ligação foi fechada pelo par.
    """
    msg = recv_chat_msg(client_sock)        
    if msg:
        print(fill(
            msg,
            width=80,
            initial_indent=(30 * ' ') + '>>> ',
            subsequent_indent=34 * ' ',
        ))
    return bool(msg)


def send_chat_msg(sock, msg):
    """
    Envia a mensagem 'msg' (str) através do socket sock. As mensagens
    enviadas devem ter dimensão fixa. Se a dimensão de msg, após 
    após codificação em bytes, for inferior a MSG_LEN bytes esta função
    acrescenta padding. 
    """
    msgb = msg.encode()
    msgb += PADDING * (MSG_LEN - len(msgb))
    sock.sendall(msgb)


def recv_chat_msg(sock):
    """
    Recebe mensagens de tamanho fixo MSG_LEN bytes. Remove eventual 
    padding. Devolve a mensagem descodificada para UTF-8.
    """
    chunks = []
    bytes_recv = 0
    while bytes_recv < MSG_LEN:
        chunk = sock.recv(min(MSG_LEN - bytes_recv, 2048))
        if chunk == b'':
            return ''
        chunks.append(chunk)
        bytes_recv += len(chunk)
    msg = b''.join(chunks).strip(PADDING).decode()
    return msg
 

def input_msg():
    """
    Lê MSG_CHARS caracteres no máximo. Fim da mensagem é sinalizado
    com SEND_CMD ou END_CMD. Devolve mensagem e comando introduzido.    
    """

    chars_left = MSG_CHARS
    lines = []
    cmd = None

    print("MSG?> ", end='')

    while cmd not in (SEND_CMD, END_CMD):        
        line = input()

        # Obtem comando no final da linha. Este pode aparecer após 
        # limite de caracteres ter sido atingido. Neste caso, linha
        # é cortada mas comando não é ignorado.
        line_end = line[line.rfind('!!'):]
        if line_end in (SEND_CMD, END_CMD):
            line, cmd = line.strip(line_end), line_end
        else:
            # Facilita contagem de caracteres se todas as linhas
            # terminarem em '\n'
            line += '\n'

        # Linha não pode exceder caracteres disponíveis
        line_len = min(len(line), chars_left)
        lines.append(line[:line_len])
        chars_left -= line_len  
        if chars_left <= 0:
            cmd = SEND_CMD 

    return ''.join(lines), cmd


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


