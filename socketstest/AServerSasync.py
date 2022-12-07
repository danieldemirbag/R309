import socket, threading
from _thread import *

print_lock = threading.Lock()

def threaded(client):
    while True:
        msgcl = client.recv(1001)
        if not msgcl:
            print('No connection, Bye')
            print_lock.release()
            break
        msgcl = msgcl[::-1]
        client.send(msgcl)
    client.close()

def server_program():
    host = "127.0.0.1"
    port = 10000

    msgcl = msgsrv = ""
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((host, port))
    server.listen(5)
    while msgcl != "arret" and msgsrv != "arret":
        conn, address = server.accept()
        print_lock.acquire()
        print('Connected to :', address[0], ':', address[1])
        start_new_thread(threaded, (conn,))
        msgcl = msgsrv = ""
        while msgcl != "bye" and msgsrv != "bye" and msgcl != "arret" and msgsrv != "arret":
            msgcl = conn.recv(1024).decode()
            print(f"Message recu : {msgcl}")
            if msgcl == "disconnect":
                conn.send("disconnect".encode())
            elif msgcl == "kill":
                conn.send("kill".encode())
            else:
                msgsrv = input("")
                conn.send(msgsrv.encode())
        conn.close()
    server.close()

if __name__ == '__main__':
    server_program()
    t1 = threading.Thread(target=server_program())
    t1.start()
    t2 = threading.Thread(target=server_program())
    t2.start()

    t1.join()  # j'attends la fin de la thread
    t2.join()  # j'attends la fin de la thread