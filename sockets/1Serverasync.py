import socket

def server_program():
    host = "127.0.0.1"
    port = 10000

    msgcl = msgsrv = ""
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((host, port))
    server.listen(5)
    while msgcl != "kill" and msgsrv != "kill":
        conn, address = server.accept()
        print('Connected to :', address[0], ':', address[1])
        msgcl = msgsrv = "> "
        while msgcl != "disconnect" and msgsrv != "disconnect" and msgcl != "kill" and msgsrv != "kill":
            msgcl = conn.recv(1024).decode()
            print(f"Message recu : {msgcl}")
            if msgcl == "disconnect":
                conn.send("disconnect".encode())
            elif msgcl == "kill":
                conn.send("kill".encode())
            else:
                msgsrv = input("> ")
                conn.send(msgsrv.encode())
        conn.close()
    server.close()

if __name__ == '__main__':
    server_program()
