import PyQt5.QtWidgets as qtw
from PyQt5.QtGui import * 
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMessageBox

import modules.vigenere as v
import modules.extendedVigenere as evig
import modules.oneTimePad as otp

cipherCache = ""

class otpWidget(qtw.QWidget):
    def __init__(self, parent):
        super(qtw.QWidget, self).__init__(parent)   
        self.initUI()
    
    def initUI(self):
        def encrypt():
            cipherCache = otp.textEncrypt(ptextBox.text())
            ctextBox.setText(v.splitStringTo5Chars(cipherCache))

        def decrypt():
            cipherCache = otp.textDecrypt(ctextBox.text())
            ptextBox.setText(v.splitStringTo5Chars(cipherCache))

        def save():
            evig.saveCipherToTextfile(ctextBox.text(),saveLine.text())
            msg = QMessageBox()
            msg.setText("File tersimpan!")
            msg.setInformativeText(f'Cipherteks berhasil disimpan pada direktori cipher/text/{saveLine.text()}.txt')
            msg.setWindowTitle("Simpan berhasil")
            msg.exec_()

        def encryptBinaryFile():
            options = qtw.QFileDialog.Options()
            options |= qtw.QFileDialog.DontUseNativeDialog
            fileName, _ = qtw.QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","All Files (*)", options=options)
            if fileName:
                try:
                    # evig.encryptBinaryFile(fileName,ktextBox.text())
                    msg = QMessageBox()
                    msg.setText(f"Filemu berhasil dienkripsi di cipher/files/encrypted_{fileName.split('/')[-1]}")
                    msg.setWindowTitle("Enkripsi Berhasil")
                    msg.exec_()
                except Exception as e:
                    print(e)

        def decryptBinaryFile():
            options = qtw.QFileDialog.Options()
            options |= qtw.QFileDialog.DontUseNativeDialog
            fileName, _ = qtw.QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","All Files (*)", options=options)
            if fileName:
                try:
                    # evig.decryptBinaryFile(fileName,ktextBox.text())
                    msg = QMessageBox()
                    msg.setText(f"Filemu berhasil dienkripsi di cipher/files/decrypted_{fileName.split('/')[-1]}")
                    msg.setWindowTitle("Enkripsi Berhasil")
                    msg.exec_()
                except Exception as e:
                    print(e)

        self.layout = qtw.QGridLayout(self)
        self.setLayout(self.layout)

        ptextLabel = qtw.QLabel("Plaintext:", self)
        ptextBox = qtw.QLineEdit(self)

        self.layout.addWidget(ptextLabel,0,0)
        self.layout.addWidget(ptextBox,1,0)

        ctextLabel = qtw.QLabel("Ciphertext:", self)
        ctextBox = qtw.QLineEdit(self)

        self.layout.addWidget(ctextLabel,0,2)
        self.layout.addWidget(ctextBox,1,2)

        buttonFileLayout = qtw.QGroupBox()
        buttonFileLayout.setLayout(qtw.QHBoxLayout())

        encryptFileButton = qtw.QPushButton("Encrypt File Text")
        encryptFileButton.clicked.connect(lambda: encryptBinaryFile())
        buttonFileLayout.layout().addWidget(encryptFileButton,0,Qt.AlignHCenter)

        decryptFileButton = qtw.QPushButton("Decrypt File Text")  
        decryptFileButton.clicked.connect(lambda: decryptBinaryFile()) 
        buttonFileLayout.layout().addWidget(decryptFileButton,1,Qt.AlignHCenter)

        self.layout.addWidget(buttonFileLayout,2,0)

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