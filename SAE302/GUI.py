from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys, socket, threading

list = ['Choisir une commande','OS', 'RAM', 'CPU', 'IP', 'Name', 'disconnect', 'kill', 'reset']

class Client(threading.Thread):

    def __init__(self, host, port):
        super().__init__()
        self.__host = host
        self.__port = port
        self.__sock = socket.socket()
    def connect(self) -> int:
        try:
            self.__sock.connect((self.__host,self.__port))
        except ConnectionRefusedError:
            msg2 = QMessageBox()
            msg2.setWindowTitle('Erreur')
            msg2.setText("serveur non lancé ou mauvaise information")
            msg2.exec_()
            return -1
        except ConnectionError:
            print ("erreur de connection")
            return -1
        else :
            print ("connexion réalisée")
            return 0
    # méthode de dialogue synchrone
    def dialogue(self):
        try:
            msg = input("client: ")
            self.__sock.send(msg.encode())
            msg = self.__sock.recv(1024).decode()
            return(msg)
        except:
            print('Serveur deconnecté !')
            self.__sock.close()
    def message(self, msg):
        self.__sock.send(msg.encode())
        rep = self.__sock.recv(1024).decode()
        return rep
    def deco(self):
        socket.socket.close()
    def run(self):
        if (self.connect() ==0):
            self.dialogue()
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.__listWidget = QListWidget()
        self.initUI()
        self.setWindowTitle("Gestionnaire de serveur")
        widget = QWidget()
        self.setCentralWidget(widget)
        grid = QGridLayout()
        widget.setLayout(grid)
        self.__list = QComboBox(self)

        self.__labIP = QLabel("IP :")
        self.__textIP = QLineEdit("")
        self.__labPORT = QLabel("PORT :")
        self.__textPORT = QLineEdit("10014")
        self.__IPlist = QComboBox()
        self.__list = QComboBox()
        for x in list:
            self.__list.addItem(x)
        self.__bouton = QPushButton("?")
        self.__envoyer = QPushButton("Envoyer")
        self.__connecter = QPushButton("Connecte")
        self.__lab = QTextEdit()
        self.__etat = QLabel("Déconnecté")
        self.__labcmd = QLabel("CMD :")
        self.__openButton = QPushButton("Ouvrir un fichier")
        layout = QVBoxLayout()
        layout.addWidget(self.__listWidget)
        layout.addWidget(self.__openButton)
        widget.setLayout(layout)

        grid.addWidget(self.__openButton, 0, 0, 1, 4)
        grid.addWidget(self.__listWidget, 1, 0, 1, 4)
        grid.addWidget(self.__labIP, 2, 0)
        grid.addWidget(self.__textIP, 2, 1)
        grid.addWidget(self.__labPORT, 2, 2)
        grid.addWidget(self.__textPORT, 2, 3)
        grid.addWidget(self.__labcmd, 4, 0)
        grid.addWidget(self.__connecter, 3, 0, 1, 4)
        grid.addWidget(self.__list, 4, 1, 1, 3)
        grid.addWidget(self.__etat, 5, 0, 1, 4)
        grid.addWidget(self.__lab, 6, 0, 1, 4)
        grid.addWidget(self.__envoyer, 7, 0)
        grid.addWidget(self.__bouton, 7, 3)


        '''self.__list.activated.connect(self._actionchanger)'''
        '''envoyer.clicked.connect(self.)'''
        self.__bouton.clicked.connect(self._messagebox)
        self.__connecter.clicked.connect(self.connection)
        self.__envoyer.clicked.connect(self.envoi_message)
        self.__openButton.clicked.connect(self.openFile)

    def openFile(self):
        fileName, _ = QFileDialog.getOpenFileName()
        if fileName:
            with open(fileName, "r") as f:
                for line in f:
                    self.__listWidget.addItem(line)

    def initUI(self):

        exitAct = QAction(QIcon('exit.png'), '&Exit', self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.setStatusTip('Exit application')
        exitAct.triggered.connect(qApp.quit)

        self.statusbar = self.statusBar()
        self.statusbar.showMessage('Ready')
        self.statusBar()

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&Plus')
        fileMenu.addAction(exitAct)
        viewMenu = menubar.addMenu('Affichage')

        viewStatAct = QAction('Theme', self, checkable=True)
        viewStatAct.setShortcut('Ctrl+N')
        viewStatAct.setStatusTip('Theme')
        viewStatAct.setChecked(False)
        viewStatAct.triggered.connect(self.toggleMenu)
        viewMenu.addAction(viewStatAct)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Simple menu')
        self.show()

    def toggleMenu(self, state):

        if state:
            self.setStyleSheet("background-color: gray;")
            """self.__textIP.setStyleSheet("background-color: white;")
            self.__textPORT.setStyleSheet("background-color: white;")
            self.__envoyer.setStyleSheet("background-color: white;")
            self.__bouton.setStyleSheet("border: solid white;")
            self.__list.setStyleSheet("border: solid white;")
            self.__lab.setStyleSheet("background-color: white;")"""
        else:
            self.setStyleSheet("background-color: light gray;")

    '''def _actionchanger(self):
        self.__lab.setText(self.__list.currentText())'''

    def _messagebox(self):
        msg = QMessageBox()
        msg.setWindowTitle("Aide")
        msg.setText("Cette application permet d'envoyer des commandes à un serveur")
        msg.exec_()

    def connection(self):
        self.conn = Client(str(self.__textIP.text()), int(self.__textPORT.text()))
        try:
            self.conn.connect()
        except:
            msg2 = QMessageBox()
            msg2.setWindowTitle('Erreur')
            msg2.setText('Erreur de connexion')
            msg2.exec_()
        else:
            self.__connecter.setEnabled(False)
            self.__connecter.show()
            self.__etat.setText('Connecté')

    def envoi_message(self):
        if self.__etat.text() == 'Connecté':
            msg = self.__list.currentText()
            try:
                if msg == 'disconnect' and msg == 'kill' and msg == 'reset':
                    self.__etat.setText('Déconnecté')
                    self.__connecter.setEnabled(True)
                    self.__connecter.show()
                    self.conn.deco()
                    self.__lab.setText('Deconnécté')
                else:
                    self.__lab.append(msg)
                    self.conn.message(msg)
                    self.__lab.append(self.conn.message(msg))
            except:
                pass
        else:
            msg2 = QMessageBox()
            msg2.setWindowTitle('Erreur')
            msg2.setText('Erreur de connexion')
            msg2.exec_()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

