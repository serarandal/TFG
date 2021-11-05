# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import sys
from PyQt5 import QtCore
from PyQt5.QtCore import QUrl,QObject,QThread,pyqtSignal,QRunnable,QThreadPool
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QLabel, QVBoxLayout
from PyQt5.QtWebEngineWidgets import QWebEngineView
import urllib3
import requests
from pynput.keyboard import Key,Listener


class FirstUi(QMainWindow):
    def __init__(self):
        super(FirstUi,self).__init__()
        self.init_ui()

    def internet_on(self):
        try:
            url = 'http://192.168.1.184'
            http = urllib3.PoolManager()
            resp = http.request('GET', url, timeout=0.1)
            if resp.status == '200': return True
        except urllib3.exceptions.HTTPError as e:
            return False

    def init_ui(self):
        self.resize(1920,1080)
        self.setWindowTitle('TFG')
        self.btn = QPushButton('config', self)
        self.btn.move(900, 500)
        if self.internet_on():
            self.helloMsg = QLabel('<h1>Connected!</h1>',self)
            self.helloMsg.move(500,100)
            self.helloMsg.adjustSize()
        else:
            self.helloMsg = QLabel('<h1>Error conection</h1>',self)
            self.helloMsg.move(500,100)
            self.helloMsg.adjustSize()
            self.btn.hide()

        self.btn.clicked.connect(self.slot_btn_function)
        self.btn2 = QPushButton('control',self)
        self.btn2.move(1200,500)
        self.btn2.clicked.connect(self.slot_btn2_function)

    def slot_btn_function(self):
        self.hide()
        self.s = SecondUi()
        self.s.show()

    def slot_btn2_function(self):

        self.hide()
        self.s = ThirdUi()
        self.s.show()


class SecondUi(QWidget):
    def __init__(self):
        super(SecondUi, self).__init__()
        self.init_ui()

    def init_ui(self):
            self.resize(1920, 1080)#Set the second window code
            self.setWindowTitle('Second Ui')#Set the second window title
            self.btn = QPushButton('GoBack', self)#Set button and button names
            self.btn.setGeometry(150, 150, 100, 50)# is the top left corner of the button, followed by the button size
            self.btn.clicked.connect(self.slot_btn_function)#Connect the signal to the slot
            self.webview = QWebEngineView()
            self.webview.load(QUrl("http://192.168.1.184"))
            lay = QVBoxLayout(self)
            lay.addWidget(self.btn)
            lay.addWidget(self.webview)

    def slot_btn_function(self):
         self.hide()# hide this window
         self.f = FirstUi()# Change the name of the first window
         self.f.show()# will display the first window


class ThirdUi(QWidget):
    def __init__(self):
        super(ThirdUi, self).__init__()
        self.init_ui()

    def init_ui(self):
        self.resize(1920,1080)
        self.setWindowTitle('ControlMotor')
        self.btn = QPushButton('GoBack', self)#Set button and button names
        self.btn.setGeometry(150, 150, 100, 50)
        self.btn.clicked.connect(self.slot_btn_function)
        self.btn2 = QPushButton('StartControl',self)
        self.btn2.setGeometry(250,250,100,100)
        self.btn2.clicked.connect(self.runTasks)

    def runTasks(self):
        threadCount = QThreadPool.globalInstance().maxThreadCount()
        pool = QThreadPool.globalInstance()
        runnable = Runnable(0)
        pool.start(runnable)

    def slot_btn_function(self):
        self.hide()
        self.s = FirstUi()
        self.s.show()




class Runnable(QRunnable):
    def __init__(self, n):
        super().__init__()
        self.n = n

    def run(self):
        def on_press(key):
            if key == key.up:
                if key == key.left:
                    r = requests.post('http://192.168.1.110:70/data/', data='180=100&')
                elif key == key.right:
                    r = requests.post('http://192.168.1.110:70/data/', data='0=100&')
                else:
                    r = requests.post('http://192.168.1.110:70/data/', data='90=100&')
            elif key == key.down:
                if key == key.left:
                    r = requests.post('http://192.168.1.110:70/data/', data='180=100&')
                elif key == key.right:
                    r = requests.post('http://192.168.1.110:70/data/', data='380=100&')
                else:
                    r = requests.post('http://192.168.1.110:70/data/', data='270=100&')

        def on_release(key):
            if key == key.esc:
                r = r = requests.post('http://192.168.1.110:70/data/', data='0,0')
                return False

        with Listener(on_press=on_press, on_release=on_release) as listener:
            listener.join()

def main():
    app = QApplication(sys.argv)
    w = FirstUi()
    w.show()
    sys.exit(app.exec())

if __name__ == '__main__':
   main()
