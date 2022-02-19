#Created by Sergio Aranda Lizano - MIT licence , see github for more instructions#
from PyQt5 import QtCore, QtGui, QtWidgets

import RealMainWindow
import ControlWindow
import ConfigWindow



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    MainWindow2 = QtWidgets.QMainWindow()
    MainWindow3 = QtWidgets.QMainWindow()
    #PopupWindow = QtWidgets.QWidget()
    ui = RealMainWindow.Ui_MainWindow()
    ui2 = ConfigWindow.Ui_MainWindow2()
    ui3 = ControlWindow.Ui_MainWindow3()
    #ui7 = PasswordWindow.Popup()
    ui.setupUi(MainWindow,MainWindow2,MainWindow3)
    ui2.setupUi(MainWindow2)
    ui3.setupUi(MainWindow3)
    #ui7.setupUi(PopupWindow)
    MainWindow.show()
    sys.exit(app.exec_())