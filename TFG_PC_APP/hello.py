import sys
import urllib3

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QWidget



def internet_on():
    try:
        url = 'http://192.168.1.184'
        http = urllib3.PoolManager()
        resp = http.request('GET', url, timeout=0.1)
        if resp.status == '200': return True
    except urllib3.exceptions.HTTPError as e:
        return False

#create instance of QApplication

app = QApplication(sys.argv)

#create instance of application's GUI

window = QWidget()
window.setWindowTitle('PyQt5 App')
window.setGeometry(100,100,1920,1080)
window.move(60,15)
if internet_on():
    helloMsg = QLabel('<h1>Connected!</h1>',parent=window)
    helloMsg.move(880,180)
else :
    helloMsg = QLabel('<h1>Error conection</h1>',parent=window)
    helloMsg.move(880,180)


#show the gui

window.show()

#run application event loop

sys.exit(app.exec())