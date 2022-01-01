from main import Ui_Window
from PyQt5 import QtWidgets as qtw
import numpy as np
from matplotlib import pyplot as plt


class TestMainWindow(qtw.QMainWindow, Ui_Window):

    def __init__(self):
        super().__init__()

        self.ui = Ui_Window()
        self.ui.setupUi(self)

        # add new process
        self.ui.pushButton.clicked.connect(self._plot)

    def _plot(self):
        print("here1")
        if not self.ui.textEdit.toPlainText():
            qtw.QMessageBox.critical(self, 'Failed', "please,Fill the equation first")
            return
        Eqn = self.ui.textEdit.toPlainText()
        print("here2")

        if not self.ui.textEdit_2.toPlainText():
            qtw.QMessageBox.critical(self, 'Failed', "please,Fill min value for x")
            return
        # if not self.ui.textEdit_2.toPlainText().isnumeric():
        #     qtw.QMessageBox.critical(self, 'Failed', "please Enter a number not anything else for min x value")
        #     return

        min_x = int(self.ui.textEdit_2.toPlainText())
        print("here3")

        if not self.ui.textEdit_3.toPlainText():
            qtw.QMessageBox.critical(self, 'Failed', "please,Fill max value for x")
            return
        # if not self.ui.textEdit_3.toPlainText().isnumeric():
        #     qtw.QMessageBox.critical(self, 'Failed', "please Enter a number not anything else for max x value")
        #     return

        max_x = int(self.ui.textEdit_3.toPlainText())
        print(max_x)
        print(min_x)
        x = np.arange(min_x, max_x+1)
        print(Eqn)
        Eqn = Eqn.replace('^', '**')
        print(Eqn)
        y = eval(Eqn)
        plt.title("Matplotlib demo")
        plt.xlabel("x axis caption")
        plt.ylabel("y axis caption")
        plt.plot(x, y)
        plt.grid(True)
        plt.show()


if __name__ == "__main__":
    app = qtw.QApplication([])
    widget1 = qtw.QStackedWidget()
    processes = TestMainWindow()
    widget1.addWidget(processes)
    widget1.show()
    app.exec_()
