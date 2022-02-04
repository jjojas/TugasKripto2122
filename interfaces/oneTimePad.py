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
            if LetterRButton.isChecked() == True:
                cipherCache = v.splitStringTo5Chars(cipherCache)
            ctextBox.setText(cipherCache)

        def decrypt():
            try:
                cipherCache = otp.textDecrypt(ctextBox.text())
                ptextBox.setText(v.splitStringTo5Chars(cipherCache))
            except Exception as e:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setText(str(e))
                msg.setWindowTitle("Dekripsi gagal")
                msg.exec_()

        def save():
            v.saveCipherToTextfile(ctextBox.text(),saveLine.text())
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
                    otp.fileEncrypt(fileName)
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
                    otp.fileDecrypt(fileName)
                    msg = QMessageBox()
                    msg.setText(f"Filemu berhasil dienkripsi di cipher/files/decrypted_{fileName.split('/')[-1]}")
                    msg.setWindowTitle("Enkripsi Berhasil")
                    msg.exec_()
                except Exception as e:
                    print(e)
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Critical)
                    msg.setText(str(e))
                    msg.setWindowTitle("Dekripsi gagal")
                    msg.exec_()

        def cipherTextState(b):
            if b.isChecked() == True:
                if b.text() == "tanpa spasi":
                    ctextBox.setText(ctextBox.text().replace(" ",""))
                elif b.text() == "per 5-huruf":
                    ctextBox.setText(v.splitStringTo5Chars(ctextBox.text()))

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

        noSpaceRButton = qtw.QRadioButton("tanpa spasi")
        noSpaceRButton.toggled.connect(lambda:cipherTextState(noSpaceRButton))
        self.layout.addWidget(noSpaceRButton,0,3)

        LetterRButton = qtw.QRadioButton("per 5-huruf")
        LetterRButton.setChecked(True)
        LetterRButton.toggled.connect(lambda:cipherTextState(LetterRButton))
        self.layout.addWidget(LetterRButton,1,3)

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

        self.layout.addWidget(saveBoxLayout,2,2,1,2)