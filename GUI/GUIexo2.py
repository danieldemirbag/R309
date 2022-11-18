import sys
from PyQt5.QtWidgets import *

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Conversion de Température")

        widget = QWidget()
        self.setCentralWidget(widget)

        grid = QGridLayout()
        widget.setLayout(grid)

        self.lab1 = QLabel("Température")
        self.lab2 = QLabel("C°")
        self.text = QLineEdit("")
        conv = QPushButton("Convertir")
        self.list = QComboBox()
        self.list.addItem("C° -> K")
        self.list.addItem("K -> C°")
        self.lab3 = QLabel("Conversion")
        self.lab4 = QLabel("")
        self.lab5 = QLabel("K")
        bouton = QPushButton("?")

        grid.addWidget(self.lab1, 0, 0)
        grid.addWidget(self.text, 0, 1)
        grid.addWidget(self.lab2, 0, 2)
        grid.addWidget(conv, 2, 1)
        grid.addWidget(self.list, 2, 3)
        grid.addWidget(self.lab3, 3, 0)
        grid.addWidget(self.lab4, 3, 1)
        grid.addWidget(self.lab5, 3, 2)
        grid.addWidget(bouton, 3, 3)


        self.list.activated.connect(self._actionchanger)
        conv.clicked.connect(self._actionconv)
        bouton.clicked.connect(self._messagebox)

    def _messagebox(self):
        msg = QMessageBox()
        msg.setWindowTitle("Aide")
        msg.setText("Permet de convertire un nombre soit de Kelvin vers Celcius, soit de Celcuis vers Kelvin")
        msg.exec_()

    def _actionchanger(self):
        if self.list.currentText() == "K -> C°":
            self.lab2.setText('K')
            self.lab5.setText('C°')
        else:
            self.lab2.setText('C°')
            self.lab5.setText('K')

    def _actionconv(self):
        msg = QMessageBox()
        msg.setWindowTitle("Erreur")
        msg.setText("La température n'est pas valide")
        try:
            x = float(self.text.text())
        except:
            msg.exec_()
        else:
            if self.list.currentText() == "K -> C°":
                x += 273.15
            else:
                x -= 273.15
            self.lab4.setText(str(x))



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()

