import sys
from PyQt5.QtWidgets import *

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        widget = QWidget()
        self.setCentralWidget(widget)

        grid = QGridLayout()
        widget.setLayout(grid)

        self.lab = QLabel("Saisir votre nom")
        self.text = QLineEdit("")
        ok = QPushButton("Ok")
        self.lab2 = QLabel("")
        quit = QPushButton("Quitter")

        grid.addWidget(self.lab, 0, 1)
        grid.addWidget(self.text, 1, 1)
        grid.addWidget(ok, 2, 1)
        grid.addWidget(self.lab2, 3, 1)
        grid.addWidget(quit, 4, 1)

        ok.clicked.connect(self._actionOk)
        quit.clicked.connect(self._actionQuitter)

        self.setWindowTitle("Une première fenêtre")

    def _actionOk(self):
        x = self.text.text()
        self.lab2.setText('Bonjour ' + x)

    def _actionQuitter(self):
        QCoreApplication.exit(0)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()