from msilib.schema import Error
import PyQt5.QtWidgets as qtw
from PyQt5.QtGui import * 
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMessageBox

import modules.fairplay as f
import modules.vigenere as vig

class playfairWidget(qtw.QWidget):
    def __init__(self, parent):
        super(qtw.QWidget, self).__init__(parent)   
        self.initUI()
    
    def initUI(self):
        def encrypt():
            cipherText = f.textEncrypt(ptextBox.text(),ktextBox.text()).upper()
            if LetterRButton.isChecked() == True:
                cipherText = vig.splitStringTo5Chars(cipherText)
            ctextBox.setText(cipherText)

        def decrypt():
            try:
                ptextBox.setText(vig.splitStringTo5Chars(f.textDecrypt(ctextBox.text(),ktextBox.text())).upper())
            except Exception as e:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setText(str(e))
                msg.setWindowTitle("Dekripsi gagal")
                msg.exec_()

        def encryptTextFile():
            if (len(ktextBox.text()) != 0):
                options = qtw.QFileDialog.Options()
                options |= qtw.QFileDialog.DontUseNativeDialog
                fileName, _ = qtw.QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","Text Files (*.txt)", options=options)
                if fileName:
                    f.fileEncrypt(str(fileName),ktextBox.text())
                    msg = QMessageBox()
                    msg.setWindowTitle("Enkripsi berhasil!")
                    msg.setText(f'File anda dapat diakses di "cipher/text/encrypted_{fileName}.txt"')
                    msg.exec_()
            else:
                msg = QMessageBox()
                msg.setText("Cipher key tidak boleh kosong!")
                msg.setWindowTitle("Enkripsi gagal")
                msg.exec_()

        def decryptTextFile():
            if (len(ktextBox.text()) != 0):
                options = qtw.QFileDialog.Options()
                options |= qtw.QFileDialog.DontUseNativeDialog
                fileName, _ = qtw.QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","Text Files (*.txt)", options=options)
                if fileName:
                    f.fileDecrypt(str(fileName),ktextBox.text())
                    msg = QMessageBox()
                    msg.setWindowTitle("Dekripsi berhasil!")
                    msg.setText(f'File anda dapat diakses di "cipher/text/decrypted_{fileName}.txt"')
                    msg.exec_()
            else:
                msg = QMessageBox()
                msg.setText("Cipher key tidak boleh kosong!")
                msg.setWindowTitle("Dekripsi gagal")
                msg.exec_()

        def save():
            vig.saveCipherToTextfile(ctextBox.text(),saveLine.text())
            msg = QMessageBox()
            msg.setText("File tersimpan!")
            msg.setInformativeText(f'Cipherteks berhasil disimpan pada direktori cipher/text/{saveLine.text()}.txt')
            msg.setWindowTitle("Simpan berhasil")
            msg.exec_()

        def cipherTextState(b):
            if b.isChecked() == True:
                if b.text() == "tanpa spasi":
                    ctextBox.setText(ctextBox.text().replace(" ",""))
                elif b.text() == "per 5-huruf":
                    ctextBox.setText(vig.splitStringTo5Chars(ctextBox.text()))

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
        encryptFileButton.clicked.connect(lambda: encryptTextFile())
        buttonFileLayout.layout().addWidget(encryptFileButton,0,Qt.AlignHCenter)

        decryptFileButton = qtw.QPushButton("Decrypt File Text")  
        decryptFileButton.clicked.connect(lambda: decryptTextFile()) 
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