import sys
from PyQt5.QtWidgets import *
from client import *
from server import *

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Gestionnaire de serveur")
        widget = QWidget()
        self.setCentralWidget(widget)
        grid = QGridLayout()
        widget.setLayout(grid)

        self.__list = QComboBox()
        self.__list.addItem("OS")
        self.__list.addItem("RAM")
        self.__list.addItem("CPU")
        self.__list.addItem("IP")
        self.__list.addItem("Name")
        self.__list.addItem("Disconnect")
        self.__list.addItem("Kill")
        self.__list.addItem("Reset")
        bouton = QPushButton("?")
        envoyer = QPushButton("Envoyer")
        self.__lab = QLabel("Choisir une commande")

        grid.addWidget(self.__list, 0, 0)
        grid.addWidget(envoyer, 2, 0)
        grid.addWidget(self.__lab, 3, 0)
        grid.addWidget(bouton, 4, 0)

        self.__list.activated.connect(self._actionchanger)
        '''envoyer.clicked.connect(self.)'''
        bouton.clicked.connect(self._messagebox)


    def _actionchanger(self):
        self.__lab.setText(self.__list.currentText() + " : ")

    def _messagebox(self):
        msg = QMessageBox()
        msg.setWindowTitle("Aide")
        msg.setText("Cette application permet d'envoyer des commandes à un serveur")
        msg.exec_()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()

