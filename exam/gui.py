from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys, socket, threading


class MainWindow(QMainWindow, threading.Thread):
    def __init__(self): # j'ai essayé (self, host, port)
        super().__init__()
        """self.__textIP = host
        self.__textPORT = port
        """
        self.__sock = socket.socket()

        self.initUI()
        self.setWindowTitle("Gestionnaire de serveur")
        widget = QWidget()
        self.setCentralWidget(widget)
        grid = QGridLayout()
        widget.setLayout(grid)


        self.__labIP = QLabel("Serveur")
        self.__textIP = QLineEdit("")
        self.__labPORT = QLabel("Port")
        self.__textPORT = QLineEdit("")
        self.__boutoncon = QPushButton("Connexion")
        self.__labmsg = QLabel("Message : ")
        self.__textmsg = QLineEdit("")
        self.__boutonsend = QPushButton("Envoyer")
        self.__boutonseff = QPushButton("Effacer")

        grid.addWidget(self.__labIP, 0, 0)
        grid.addWidget(self.__textIP, 0, 1)
        grid.addWidget(self.__labPORT, 1, 0)
        grid.addWidget(self.__textPORT, 1, 1)
        grid.addWidget(self.__boutoncon, 2, 0, 1, 2)
        grid.addWidget(self.__labmsg, 4, 0)
        grid.addWidget(self.__textmsg, 4, 1)
        grid.addWidget(self.__boutonsend, 5, 0, 1, 2)
        grid.addWidget(self.__boutonseff, 6, 0, 1, 2)

        self.__boutoncon.clicked.connect(self._actionCon)


    def _actionCon(self) -> int:
        if self.__textIP.currentText() == "localhost" and self.__textPORT.currentText() == 10000:
            try:
                """self.__sock.connect((self.__host, self.__port))"""
                self.__sock.connect((self.__textIP, self.__textPORT))
            except ConnectionRefusedError:
                print("serveur non lancé ou mauvaise information")
                return -1
            except ConnectionError:
                print("erreur de connection")
                return -1
            else:
                print("connexion réalisée")
                return 0
    def __dialogue(self):
        msg = ""
        while msg != "kill" and msg != "disconnect" and msg != "reset":
            msg = input("client: ")
            self.__sock.send(msg.encode())
            msg = self.__sock.recv(1024).decode()
        self.__sock.close()


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

    def _actionchanger(self):
        self.__lab.setText(self.__list.currentText() + " : ")



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

