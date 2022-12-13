import socket, threading

host = "127.0.0.1"
port = 10000
server = socket.socket()
server.bind((host, port))
server.listen(2)
conn, address = server.accept()

def ecoute():
    while True:
        msg = conn.recv(1024).decode()
        if not msg or msg == 'bye':
            break
        print('Message recu : ' + msg)
    conn.close()
    print('Déconnexion...')

def message():
    while True:
        msg = input()
        if msg != 'arret':
            conn.send(msg.encode())
        else:
            break
    conn.close()
    server.close()
    print("Fermeture du server...")

if __name__ == '__main__':

    t1 = threading.Thread(target=message)
    t1.start()
    t2 = threading.Thread(target=ecoute)
    t2.start()

    t1.join()
    t2.join()