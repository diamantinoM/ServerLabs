
from socket import socket, AF_INET, SOCK_STREAM, SOL_SOCKET, SO_REUSEADDR


CHUNK_DIM = 4096


def tcp_file_server(bind_addr, server_port):
    # INET (IPv4) streaming socket 
    serv_socket = socket(AF_INET, SOCK_STREAM)    
    # So that we can reuse the same addr if we restart the server and
    # there are pending client connections (otherwise we must wait for 
    # aprox ~2m before the OS releases the addr to another program)
    serv_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, True)
    # bind socket to IP address and serv_port
    serv_socket.bind((bind_addr, server_port))    
    # become a server socket
    serv_socket.listen(5)

    print("Waiting for connections on {} {}".format(bind_addr, server_port))

    # Serve forever
    while True:
        client_sock, client_addr = serv_socket.accept()
        file_handler(client_sock, client_addr)


def file_handler(client_sock, client_addr):
    print("Got a connection from {}".format(client_addr))

    with open('alberto.bin', 'wb') as file:    
        while True:
            chunk = client_sock.recv(CHUNK_DIM)
            if not chunk:
                break
            file.write(chunk)
    client_sock.close()


if __name__ == '__main__':
    tcp_file_server('', 15424)
