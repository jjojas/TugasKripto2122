import PyQt5.QtWidgets as qtw
from PyQt5.QtGui import * 
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMessageBox

import modules.vigenere as vig

class vigenereWidget(qtw.QWidget):
    def __init__(self, parent):
        super(qtw.QWidget, self).__init__(parent)   
        self.initUI()
    
    def initUI(self):
        def encrypt():
            ctextBox.setText(vig.splitStringTo5Chars(vig.vigenereEncrypt(ptextBox.text(),ktextBox.text())))

        def decrypt():
            ptextBox.setText(vig.splitStringTo5Chars(vig.vigenereDecrypt(ctextBox.text(),ktextBox.text())))

        def save():
            vig.saveCipherToTextfile(ctextBox.text(),saveLine.text())
            msg = QMessageBox()
            msg.setText("File tersimpan!")
            msg.setInformativeText(f'Cipherteks berhasil disimpan pada direktori cipher/text/{saveLine.text()}.txt')
            msg.setWindowTitle("Simpan berhasil")
            msg.exec_()

        self.layout = qtw.QGridLayout(self)
        self.setLayout(self.layout)

        ptextLabel = qtw.QLabel("Plaintext:", self)
        ptextBox = qtw.QLineEdit(self)

        self.layout.addWidget(ptextLabel,0,0)
        self.layout.addWidget(ptextBox,1,0)

        ktextLabel = qtw.QLabel("Key:", self)
        ktextBox = qtw.QLineEdit(self)

        self.layout.addWidget(ktextLabel,0,1)
        self.layout.addWidget(ktextBox,1,1)

        ctextLabel = qtw.QLabel("Ciphertext:", self)
        ctextBox = qtw.QLineEdit(self)

        self.layout.addWidget(ctextLabel,0,2)
        self.layout.addWidget(ctextBox,1,2)

        buttonLayout = qtw.QGroupBox()
        buttonLayout.setLayout(qtw.QHBoxLayout())
    
        encryptButton = qtw.QPushButton("Encrypt")
        encryptButton.clicked.connect(lambda: encrypt())
        buttonLayout.layout().addWidget(encryptButton,0,Qt.AlignHCenter)

        decryptButton = qtw.QPushButton("Decrypt")  
        decryptButton.clicked.connect(lambda: decrypt()) 
        buttonLayout.layout().addWidget(decryptButton,1,Qt.AlignHCenter)

        self.layout.addWidget(buttonLayout,2,1)

        saveBoxLayout = qtw.QGroupBox()
        saveBoxLayout.setLayout(qtw.QVBoxLayout())
        saveLabel = qtw.QLabel("Filename:", self)
        saveLine = qtw.QLineEdit(self)
        saveButton = qtw.QPushButton("Save Ciphertext")  
        saveButton.clicked.connect(lambda: save()) 

        saveBoxLayout.layout().addWidget(saveLabel,0,Qt.AlignHCenter)
        saveBoxLayout.layout().addWidget(saveLine,1,Qt.AlignHCenter)
        saveBoxLayout.layout().addWidget(saveButton,2,Qt.AlignHCenter)

        self.layout.addWidget(saveBoxLayout,2,2)



