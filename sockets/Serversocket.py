import socket, sys

def server():
    reply = input('ffff')
    host = '127.0.0.1'
    port = 10000
    server_socket = socket.socket()
    server_socket.bind((host, port))
    server_socket.listen(10)
    conn, address = server_socket.accept()
    data = conn.recv(1024).decode()
    print(data)
    conn.send(reply.encode())
    conn.close()

if __name__ == '__main__':
    sys.exit(server())