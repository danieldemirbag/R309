import socket, threading
from _thread import *

def client_program():
    host = "127.0.0.1"
    port = 10000

    client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    client.connect((host, port))
    msgcl = msgsrv = "> "
    while msgcl != "bye" and msgsrv != "bye" and msgcl != "arret" and msgsrv != "arret":
        msgcl = input("> ")
        client.send(msgcl.encode())
        msgsrv = client.recv(1024).decode()
        print(f"Message recu : {msgsrv}")
    client.close()

if __name__ == '__main__':
    client_program()