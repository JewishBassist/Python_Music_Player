from PyQt5 import QtWidgets
import sys
from ui import Ui_Dialog
import numpy as np

if __name__ == "__main__":
    # Создаём приложение
    app = QtWidgets.QApplication(sys.argv)
    # Создаём форму (диалог)
    Dialog = QtWidgets.QWidget()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()

    # Создаём коллекцию list
    listOriginal = ["מיה סולימן - לאט", "Berry Sakharof - יומולדת", "כולם מזיזים - Anna Zak"]

    f_buttonOnOff = False

    def button_on_off():
        global f_buttonOnOff
        if not f_buttonOnOff:
            f_buttonOnOff = True
            button_on()
            return
        if f_buttonOnOff:
            f_buttonOnOff = False
            button_off()

    ui.pushButton_4.clicked.connect(button_on_off)

    def button_on():
        for x in listOriginal:
            ui.listWidget.addItem(x)
        ui.pushButton_4.setText("OFF")
        ui.pushButton_4.setStyleSheet("QPushButton{background-color: green; color: white}")

    def button_off():
        ui.listWidget.clear()
        ui.pushButton_4.setText("ON")
        ui.pushButton_4.setStyleSheet("QPushButton{background-color: red; color: black}")

    def shuffle(self):
        ui.listWidget.clear()
        listRandomized = np.random.permutation(listOriginal)
        for x in listRandomized:
            ui.listWidget.addItem(x)

    sys.exit(app.exec_())
