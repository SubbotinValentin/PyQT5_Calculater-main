from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication, QMenuBar, QMenu, QMainWindow, \
    QFileDialog  # Импортируем класс для создания множества окон в одном приложении.

import sys


class Window(QMainWindow):  # Создал класс для конструктора

    def __init__(self): # Инициализировал класс конструктора Window
        super(Window, self).__init__()

        self.setWindowTitle("Редактор кода")
        self.setGeometry(100, 100, 600, 400)

        self.text_edit = QtWidgets.QTextEdit(self)
        self.setCentralWidget(self.text_edit)

        self.createMenuBar()

    def createMenuBar(self):
        self.menuBar = QMenuBar(self)
        self.setMenuBar(self.menuBar)

        fileMenu = QMenu("&Файл", self)
        self.menuBar.addMenu(fileMenu)

        fileMenu.addAction("Открыть", self.action_clicked)
        fileMenu.addAction("Сохранить", self.action_clicked)

    @QtCore.pyqtSlot()
    def action_clicked(self):
        action = self.sender()
        if action.text() == 'Открыть':
            fname = QFileDialog.getOpenFileName(self)[0]

            try:
                f = open(fname, 'r')
                with f:
                    data = f.read()
                    self.text_edit.setText(data)
                f.close()
            except FileNotFoundError:
                print("No such file")

        elif action.text() == 'Сохранить':
            fname = QFileDialog.getSaveFileName(self)[0]

            try:
                f = open(fname, 'w')
                text = self.text_edit.toPlainText()
                f.write(text)
                f.close()
            except FileNotFoundError:
                print("No such file")


def application():
    app = QApplication(sys.argv)
    window = Window()

    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    application()