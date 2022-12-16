import socket, platform ,subprocess, os
import psutil as psutil


def serveur():
    msg = ""
    conn = None
    server_socket = None
    while msg != "kill":
        msg = ""
        server_socket = socket.socket()
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.bind(("0.0.0.0", 10014))
        server_socket.listen(1)
        print('Serveur en attente de connexion')
        while msg != "kill" and msg != "reset":
            msg = ""
            try:
                conn, addr = server_socket.accept()
                print(addr)
            except ConnectionError:
                print ("erreur de connection")
                break
            else :
                while msg != "kill" and msg != "reset" and msg != "disconnect":
                    msg = conn.recv(1024).decode()
                    print ("Received from client: ", msg)
                    if msg == "OS":
                        msg = subprocess.getoutput('systeminfo | findstr /C:"Nom du système d’exploitation:"') + \
                              '\n' + subprocess.getoutput('systeminfo | findstr /C:"Version du système:"')
                    elif msg == "RAM":
                        msgRAM = psutil.virtual_memory().total / 1000000000
                        msgRAM1 = psutil.virtual_memory().available * 100 / psutil.virtual_memory().total
                        msgRAM2 = psutil.virtual_memory().percent
                        msg = (f'RAM : {round(msgRAM)} Go | RAM utilisée : {round(msgRAM2)} % | RAM disponible : {round(msgRAM1)} %')
                    elif msg == "CPU":
                        msg = (f'Utilisation du CPU : {psutil.cpu_percent()} %')
                    elif msg == "IP":
                        msg = "Les IP disponible sur le server sont : \n" + subprocess.getoutput('ipconfig | findstr /i "Adresse IPv4"')
                    elif msg == "Name":
                        msg = 'Le nom de la machine est : ' + subprocess.getoutput('hostname')
                    conn.send(msg.encode())
                conn.close()
        print ("Connection closed")
        server_socket.close()
        print ("Server closed")

if __name__ == '__main__':
    serveur()