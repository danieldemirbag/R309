import sys
from PyQt5.QtWidgets import *

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        widget = QWidget()
        self.setCentralWidget(widget)

        grid = QGridLayout()
        widget.setLayout(grid)

        self.lab1 = QLabel("Température")
        self.lab2 = QLabel("")
        self.text = QLineEdit("")
        conv = QPushButton("Convertir")
        self.list = QComboBox()
        self.list.addItem(["C° -> K", "K -> C°"])

        grid.addWidget(self.lab1, 0, 1)
        grid.addWidget(self.text, 0, 2)
        grid.addWidget(self.lab2, 0, 3)
        grid.addWidget(conv, 2, 2)

        self.setWindowTitle("Conversion de Température")