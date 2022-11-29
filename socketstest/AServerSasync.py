import socket, threading


def server_program():
    host = "127.0.0.1"
    port = 5000

    msgcl = msgsrv = ""
    server = socket.socket()
    server.bind((host, port))
    server.listen(2)
    while msgcl != "arret" and msgsrv != "arret":
        conn, address = server.accept()
        msgcl = msgsrv = ""
        while msgcl != "bye" and msgsrv != "bye" and msgcl != "arret" and msgsrv != "arret":
            msgcl = conn.recv(1024).decode()
            print(f"Message recu : {msgcl}")
            if msgcl == "bye":
                conn.send("bye".encode())
            elif msgcl == "arret":
                conn.send("arret".encode())
            else:
                msgsrv = input("")
                conn.send(msgsrv.encode())
        conn.close()
    server.close()

if __name__ == '__main__':
    t1 = threading.Thread(target=server_program())
    t1.start()
    t2 = threading.Thread(target=server_program())
    t2.start()

    t1.join()  # j'attends la fin de la thread
    t2.join()  # j'attends la fin de la thread