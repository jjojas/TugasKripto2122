import PyQt5.QtWidgets as qtw
from PyQt5.QtGui import * 

import interfaces.vigenere as v
import interfaces.extendedVigenere as ev
import interfaces.fairplayCipher as p
import interfaces.oneTimePad as otp
import interfaces.enigma as e

from os import environ

def suppress_qt_warnings():
    environ["QT_DEVICE_PIXEL_RATIO"] = "0"
    environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
    environ["QT_SCREEN_SCALE_FACTORS"] = "1"
    environ["QT_SCALE_FACTOR"] = "1"

class mainWidget(qtw.QWidget):
    def __init__(self, parent):
        super(qtw.QWidget, self).__init__(parent)   
        self.initUI()
    
    def initUI(self):
        '''
        Menginisialisasi antarmuka utama
        '''
        self.layout = qtw.QHBoxLayout(self)
        self.tabs = qtw.QTabWidget()
        self.tabs.setFont(QFont('Roboto', 14))
        self.tabs.addTab(v.vigenereWidget(self),"Vigenere")
        self.tabs.addTab(ev.extendedVigenereWidget(self),"Extended Vigenere")
        self.tabs.addTab(p.playfairWidget(self),"Playfair")
        self.tabs.addTab(e.enigmaWidget(self),"Enigma")
        self.tabs.addTab(otp.otpWidget(self),"One-time-pad")
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)    

class MainWindow(qtw.QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Tugas Kecil 1 - Kriptografi dan Koding")
        # self.setGeometry(0, 0, 1920, 1080)
        self.mainWidget = mainWidget(self)
        self.setCentralWidget(self.mainWidget)
        self.show()

suppress_qt_warnings()

app = qtw.QApplication([])
mw = MainWindow()

app.exec_()
