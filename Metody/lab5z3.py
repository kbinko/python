import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
QWidget, QPushButton, QLabel,
QGridLayout, QLineEdit, QApplication, QMessageBox
)
from matplotlib.pyplot import plot, show
from scipy import interpolate
from numpy import arange, exp

class Program(QWidget):
    def __init__(self):
        super().__init__()

        self.lbl1 = QLabel('Podaj: xp, xk, krok (oddziel przecinkiem)') # etykiety
        self.lbl2 = QLabel('Uruchom') # etykieta
        self.btn1 = QPushButton('GO') # przycisk
        self.text1 = QLineEdit() # pole tekstowe

        # siatka pomaga w rozmieszczeniu obiektów
        siatka = QGridLayout()
        siatka.setSpacing(10)

        siatka.addWidget(self.lbl1, 1, 0) # dodaj etykietę
        siatka.addWidget(self.text1, 1, 1) # dodaj pole tekstowe

        siatka.addWidget(self.lbl2, 2, 0) # dodaj etykietę
        siatka.addWidget(self.btn1, 2, 1) # dodaj przycisk

        self.setLayout(siatka) # włącz siatkę

        # zdarzenia
        self.btn1.clicked.connect(self.btn1Clicked)

        self.setGeometry(300, 300, 450, 150)
        self.setWindowTitle('Przykład: pole/przycisk')
        self.show()

    def btn1Clicked(self):
        sender = self.sender()
        txt1 = self.text1.text()
        txt1split = txt1.split(',')
        txt1final = 'xp=' + txt1split[0] + ' xk=' + txt1split[1] + ' krok=' + txt1split[2]
        self.text1.clear()
        self.text1.insert(txt1final)

        try:
            xp = float(txt1split[0])
            xk = float(txt1split[1])
            k = float(txt1split[2])
            self.interpolacja(xp, xk, k)
        except ValueError:
            QMessageBox.critical(self, 'Błąd', 'Nieprawidłowe dane wejściowe. Wprowadź poprawne liczby.')

    def interpolacja(self, xp, xk, k):
        x = arange(xp, xk, 1)
        y = exp(-x / 3.0)

        # użycie funkcji interpolującej 'interpolate.interp1d'
        f = interpolate.interp1d(x, y, kind='cubic')
        xnew = arange(xp, x[-1], k)
        ynew = f(xnew) # obliczenie interpolacji
        plot(x, y, 'o', xnew, ynew, '-')
        show()

    if __name__ == '__main__':
        app = QApplication(sys.argv)
        program = Program()
        sys.exit(app.exec_())