from PyQt5 import QtWidgets
import sys
from ui import Ui_Dialog
import numpy as np

class MusicPlayer:
    def __init__(self):
        self.app = QtWidgets.QApplication(sys.argv)
        self.Dialog = QtWidgets.QWidget()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self.Dialog)
        self.Dialog.show()
        self.listOriginal = ["מיה סולימן - לאט", "Berry Sakharof - יומולדת", "כולם מזיזים - Anna Zak"]
        self.f_buttonOnOff = False
        self.ui.pushButton_4.clicked.connect(self.button_on_off)
        self.ui.pushButton.clicked.connect(self.shuffle)


    def button_on_off(self):
        if not self.f_buttonOnOff:
            self.f_buttonOnOff = True
            self.button_on()
            return
        if self.f_buttonOnOff:
            self.f_buttonOnOff = False
            self.button_off()

    def button_on(self):
        for x in self.listOriginal:
            self.ui.listWidget.addItem(x)
        self.ui.pushButton_4.setText("OFF")
        self.ui.pushButton_4.setStyleSheet("QPushButton{background-color: green; color: white}")

    def button_off(self):
        self.ui.listWidget.clear()
        self.ui.pushButton_4.setText("ON")
        self.ui.pushButton_4.setStyleSheet("QPushButton{background-color: red; color: black}")

    def shuffle(self):
        self.ui.listWidget.clear()
        list_randomized = np.random.permutation(self.listOriginal)
        for x in list_randomized:
            self.ui.listWidget.addItem(x)

    def run(self):
        sys.exit(self.app.exec_())

if __name__ == "__main__":
    player = MusicPlayer()
    player.run()
