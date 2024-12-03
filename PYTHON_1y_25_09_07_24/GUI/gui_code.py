import sys
from PyQt6 import QtWidgets, uic
from first_gui import Ui_Form


class MainWindow(QtWidgets.QMainWindow, Ui_Form):

    def __init__(self, *args, obj=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.Plus.clicked.connect(self.plus_clicked)
        self.Minus.clicked.connect(self.minus_clicked)
        self.Multiply.clicked.connect(self.multiply_clicked)
        self.Divine.clicked.connect(self.divine_clicked)

    def plus_clicked(self):
        number_1 = float(self.FirstNumber.text())
        number_2 = float(self.SecondNumber.text())
        result = number_1 + number_2
        self.HelloLabel.setText(str(result))
        self.FirstNumber.clear()
        self.SecondNumber.clear()

    def minus_clicked(self):
        number_1 = float(self.FirstNumber.text())
        number_2 = float(self.SecondNumber.text())
        result = number_1 - number_2
        self.HelloLabel.setText(str(result))
        self.FirstNumber.clear()
        self.SecondNumber.clear()

    def multiply_clicked(self):
        number_1 = float(self.FirstNumber.text())
        number_2 = float(self.SecondNumber.text())
        result = number_1 * number_2
        self.HelloLabel.setText(str(result))
        self.FirstNumber.clear()
        self.SecondNumber.clear()

    def divine_clicked(self):
        number_1 = float(self.FirstNumber.text())
        number_2 = float(self.SecondNumber.text())
        result = number_1 / number_2
        self.HelloLabel.setText(str(result))
        self.FirstNumber.clear()
        self.SecondNumber.clear()


app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
