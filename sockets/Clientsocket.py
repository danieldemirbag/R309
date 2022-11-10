import socket, sys

def client():
    message = print(input("Entrez votre message : "))
    host = '127.0.0.1'
    port = 10000
    client_socket = socket.socket()
    client_socket.connect((host, port))
    client_socket.send(message.encode())
    data = client_socket.recv(1024).decode()
    print(data)
    client_socket.close()

if __name__ == '__main__':
    sys.exit(client())