import socket, threading


def client_program():
    host = "127.0.0.1"
    port = 5000

    client = socket.socket()
    client.connect((host, port))
    msgcl = msgsrv = "> "
    while msgcl != "bye" and msgsrv != "bye" and msgcl != "arret" and msgsrv != "arret":
        msgcl = input("> ")
        client.send(msgcl.encode())
        msgsrv = client.recv(1024).decode()
        print(f"Message recu : {msgsrv}")
    client.close()

if __name__ == '__main__':
    t1 = threading.Thread(target=client_program())
    t1.start()
    t2 = threading.Thread(target=client_program())
    t2.start()

    t1.join()  # j'attends la fin de la thread
    t2.join()  # j'attends la fin de la thread