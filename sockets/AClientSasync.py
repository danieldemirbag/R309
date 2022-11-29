import socket, threading

host = "127.0.0.1"
port = 10000
client = socket.socket()
client.connect((host, port))

def ecoute():
    while True:
        msg = client.recv(1024).decode()
        if not msg or msg == 'bye':
            break
        print('Reponse du serveur : ' + msg)
    client.close()
    print('Déconnexion...')
    client.connect((host, port))

def message():
    while True:
        msg = input()
        client.send(msg.encode())



if __name__ == '__main__':

    t1 = threading.Thread(target=message)
    t1.start()
    t2 = threading.Thread(target=ecoute)
    t2.start()

    t1.join()
    t2.join()
