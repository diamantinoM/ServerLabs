from socket import socket, AF_INET, SOCK_STREAM


CHUNK_DIM = 4096


def tcp_file_client(server_addr, server_port, filepath):
    sock = socket(AF_INET, SOCK_STREAM)
    sock.connect((server_addr, server_port))

    with open(filepath, 'rb') as file:
        while True:
            chunk = file.read(CHUNK_DIM)
            if not chunk:
                print("Ficheiro enviado")
                break
            sock.sendall(chunk)
    sock.close()    


if __name__ == '__main__':
    addr = input('Endereço? [localhost] ')
    if not addr.strip():
        addr = 'localhost'
    port = input('Porto? [15424] ')
    if not port.strip():
        port = 15424
    else:
        port = int(port)
    filename = input("Caminho para o ficheiro: ")
    tcp_file_client(addr, port, filename)