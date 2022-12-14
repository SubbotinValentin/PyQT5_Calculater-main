from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox


class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 300)
        self.calculator = QtWidgets.QWidget(MainWindow)
        self.calculator.setObjectName("calculator")
        self.label = QtWidgets.QLabel(self.calculator)
        self.label.setEnabled(True)
        self.label.setGeometry(QtCore.QRect(0, 0, 400, 100))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setFocusPolicy(QtCore.Qt.TabFocus)
        self.label.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.label.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.label.setScaledContents(False)
        self.label.setAlignment(QtCore.Qt.AlignBottom | QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing)
        self.label.setWordWrap(False)
        self.label.setIndent(0)
        self.label.setOpenExternalLinks(False)
        self.label.setObjectName("label")
        self.button7 = QtWidgets.QPushButton(self.calculator)
        self.button7.setGeometry(QtCore.QRect(0, 100, 100, 50))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.button7.setFont(font)
        self.button7.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.button7.setObjectName("button7")
        self.button8 = QtWidgets.QPushButton(self.calculator)
        self.button8.setGeometry(QtCore.QRect(100, 100, 100, 50))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.button8.setFont(font)
        self.button8.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.button8.setObjectName("button8")
        self.button9 = QtWidgets.QPushButton(self.calculator)
        self.button9.setGeometry(QtCore.QRect(200, 100, 100, 50))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.button9.setFont(font)
        self.button9.setMouseTracking(False)
        self.button9.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.button9.setObjectName("button9")
        self.buttonSum = QtWidgets.QPushButton(self.calculator)
        self.buttonSum.setGeometry(QtCore.QRect(300, 100, 100, 50))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.buttonSum.setFont(font)
        self.buttonSum.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.buttonSum.setObjectName("buttonSum")
        self.buttonUnsum = QtWidgets.QPushButton(self.calculator)
        self.buttonUnsum.setGeometry(QtCore.QRect(300, 150, 100, 50))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.buttonUnsum.setFont(font)
        self.buttonUnsum.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.buttonUnsum.setObjectName("buttonUnsum")
        self.buttonMas = QtWidgets.QPushButton(self.calculator)
        self.buttonMas.setGeometry(QtCore.QRect(300, 200, 100, 50))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.buttonMas.setFont(font)
        self.buttonMas.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.buttonMas.setObjectName("buttonMas")
        self.buttonUnmas = QtWidgets.QPushButton(self.calculator)
        self.buttonUnmas.setGeometry(QtCore.QRect(300, 250, 100, 50))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.buttonUnmas.setFont(font)
        self.buttonUnmas.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.buttonUnmas.setObjectName("buttonUnmas")
        self.buttonUnsum_2 = QtWidgets.QPushButton(self.calculator)
        self.buttonUnsum_2.setGeometry(QtCore.QRect(200, 250, 100, 50))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.buttonUnsum_2.setFont(font)
        self.buttonUnsum_2.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.buttonUnsum_2.setObjectName("buttonUnsum_2")
        self.button4 = QtWidgets.QPushButton(self.calculator)
        self.button4.setGeometry(QtCore.QRect(0, 150, 100, 50))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.button4.setFont(font)
        self.button4.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.button4.setObjectName("button4")
        self.button5 = QtWidgets.QPushButton(self.calculator)
        self.button5.setGeometry(QtCore.QRect(100, 150, 100, 50))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.button5.setFont(font)
        self.button5.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.button5.setObjectName("button5")
        self.button6 = QtWidgets.QPushButton(self.calculator)
        self.button6.setGeometry(QtCore.QRect(200, 150, 100, 50))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.button6.setFont(font)
        self.button6.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.button6.setObjectName("button6")
        self.button1 = QtWidgets.QPushButton(self.calculator)
        self.button1.setGeometry(QtCore.QRect(0, 200, 100, 50))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.button1.setFont(font)
        self.button1.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.button1.setObjectName("button1")
        self.button2 = QtWidgets.QPushButton(self.calculator)
        self.button2.setGeometry(QtCore.QRect(100, 200, 100, 50))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.button2.setFont(font)
        self.button2.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.button2.setObjectName("button2")
        self.button3 = QtWidgets.QPushButton(self.calculator)
        self.button3.setGeometry(QtCore.QRect(200, 200, 100, 50))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.button3.setFont(font)
        self.button3.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.button3.setObjectName("button3")
        self.button0 = QtWidgets.QPushButton(self.calculator)
        self.button0.setGeometry(QtCore.QRect(100, 250, 100, 50))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.button0.setFont(font)
        self.button0.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.button0.setObjectName("button0")
        self.buttonC = QtWidgets.QPushButton(self.calculator)
        self.buttonC.setGeometry(QtCore.QRect(0, 250, 100, 50))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.buttonC.setFont(font)
        self.buttonC.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.buttonC.setObjectName("buttonC")
        MainWindow.setCentralWidget(self.calculator)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.add_functions()

        self.is_equal = False

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "0"))
        self.button7.setText(_translate("MainWindow", "7"))
        self.button8.setText(_translate("MainWindow", "8"))
        self.button9.setText(_translate("MainWindow", "9"))
        self.buttonSum.setText(_translate("MainWindow", "+"))
        self.buttonUnsum.setText(_translate("MainWindow", "-"))
        self.buttonMas.setText(_translate("MainWindow", "*"))
        self.buttonUnmas.setText(_translate("MainWindow", "/"))
        self.buttonUnsum_2.setText(_translate("MainWindow", "="))
        self.button4.setText(_translate("MainWindow", "4"))
        self.button5.setText(_translate("MainWindow", "5"))
        self.button6.setText(_translate("MainWindow", "6"))
        self.button1.setText(_translate("MainWindow", "1"))
        self.button2.setText(_translate("MainWindow", "2"))
        self.button3.setText(_translate("MainWindow", "3"))
        self.button0.setText(_translate("MainWindow", "0"))
        self.buttonC.setText(_translate("MainWindow", "C"))

    def add_functions(self):
        self.button0.clicked.connect(lambda: self.write_number(self.button0.text()))
        self.button1.clicked.connect(lambda: self.write_number(self.button1.text()))
        self.button2.clicked.connect(lambda: self.write_number(self.button2.text()))
        self.button3.clicked.connect(lambda: self.write_number(self.button3.text()))
        self.button4.clicked.connect(lambda: self.write_number(self.button4.text()))
        self.button5.clicked.connect(lambda: self.write_number(self.button5.text()))
        self.button6.clicked.connect(lambda: self.write_number(self.button6.text()))
        self.button7.clicked.connect(lambda: self.write_number(self.button7.text()))
        self.button8.clicked.connect(lambda: self.write_number(self.button8.text()))
        self.button9.clicked.connect(lambda: self.write_number(self.button9.text()))
        self.buttonSum.clicked.connect(lambda: self.write_number(self.buttonSum.text()))
        self.buttonUnsum.clicked.connect(lambda: self.write_number(self.buttonUnsum.text()))
        self.buttonMas.clicked.connect(lambda: self.write_number(self.buttonMas.text()))
        self.buttonUnmas.clicked.connect(lambda: self.write_number(self.buttonUnsum.text()))
        self.buttonC.clicked.connect(lambda: self.write_number(self.buttonC.text()))

        self.buttonUnsum_2.clicked.connect(self.results)

    def write_number(self, number):
        if self.label.text() == "0" or self.is_equal:
            self.label.setText(number)
            self.is_equal = False
        else:
            self.label.setText(self.label.text() + number)

    def results(self):
        if not self.is_equal:
            res = eval(self.label.text())
            self.label.setText("??????????????????: " + str(res))
            self.is_equal = True
        else:
            error = QMessageBox()
            error.setWindowTitle("????????????")
            error.setText("???????????? ?????? ???????????????? ?????????????????? ????????????")
            error.setIcon(QMessageBox.Warning)
            error.setStandardButtons(QMessageBox.Ok | QMessageBox.Reset | QMessageBox.Cancel)
            error.setDefaultButton(QMessageBox.Ok)
            error.setInformativeText("?????? ???????? ???????????????? ???? ??????????????????????")
            error.setDetailedText("????????????...")

            error.buttonClicked.connect(self.popup_action)

            error.exec_()

    def popup_action(self, button):
        if button.text() == "Ok":
            print("Ok")
        elif button.text() == "Reset":
            self.label.setText("")
            self.is_equal = False


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
