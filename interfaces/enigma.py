import PyQt5.QtWidgets as qtw
from PyQt5.QtGui import * 
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMessageBox

import modules.vigenere as v
import modules.enigma as en

cipherCache = ""

class enigmaWidget(qtw.QWidget):
    def __init__(self, parent):
        super(qtw.QWidget, self).__init__(parent)   
        self.initUI()
    
    def initUI(self):
        def encrypt():
            cipherCache = en.textEncryptAndDecypt(ptextBox.text(),lrotorLabel.text(),mrotorLabel.text(),rrotorLabel.text())
            if LetterRButton.isChecked() == True:
                cipherCache = v.splitStringTo5Chars(cipherCache)
            ctextBox.setText(cipherCache.upper())
            

        def decrypt():
            decipherCache = en.textEncryptAndDecypt(ctextBox.text(),lrotorLabel.text(),mrotorLabel.text(),rrotorLabel.text())
            ptextBox.setText(v.splitStringTo5Chars(decipherCache.upper()))

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
            fileName, _ = qtw.QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","Text Files (*.txt)", options=options)
            if fileName:
                try:
                    en.fileEncrypt(fileName,lrotorLabel.text(),mrotorLabel.text(),rrotorLabel.text())
                    msg = QMessageBox()
                    msg.setText(f"Filemu berhasil dienkripsi di cipher/files/encrypted_{fileName.split('/')[-1]}")
                    msg.setWindowTitle("Enkripsi Berhasil")
                    msg.exec_()
                except Exception as e:
                    print(e)

        def decryptBinaryFile():
            options = qtw.QFileDialog.Options()
            options |= qtw.QFileDialog.DontUseNativeDialog
            fileName, _ = qtw.QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","Text Files (*.txt)", options=options)
            if fileName:
                try:
                    en.fileDecrypt(fileName,lrotorLabel.text(),mrotorLabel.text(),rrotorLabel.text())
                    msg = QMessageBox()
                    msg.setText(f"Filemu berhasil dienkripsi di cipher/files/decrypted_{fileName.split('/')[-1]}")
                    msg.setWindowTitle("Enkripsi Berhasil")
                    msg.exec_()
                except Exception as e:
                    print(e)

        def valuechangel():
            lrotorLabel.setText(chr(64+(lrotorSpinbox.value())))

        def valuechangem():
            mrotorLabel.setText(chr(64+(mrotorSpinbox.value())))
            
        def valuechanger():
            rrotorLabel.setText(chr(64+(rrotorSpinbox.value())))

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

        # ktextLabel = qtw.QLabel("Key:", self)
        # ktextBox = qtw.QLineEdit(self)

        # self.layout.addWidget(ktextLabel,0,1)
        # self.layout.addWidget(ktextBox,1,1)

        rlayout = qtw.QGroupBox(self)
        rlayout.setLayout(qtw.QGridLayout())

        rtextLabel = qtw.QLabel("Initial Rotor", self)
        self.layout.addWidget(rtextLabel,0,1)
        # rlayout.layout().addWidget(rtextLabel,0,1)

        lrotorLabel = qtw.QLabel("A",self)
        lrotorSpinbox = qtw.QSpinBox(self)
        lrotorSpinbox.setRange(1,26)
        lrotorSpinbox.valueChanged.connect(lambda: valuechangel())

        rlayout.layout().addWidget(lrotorLabel,1,1)
        rlayout.layout().addWidget(lrotorSpinbox,2,1)

        mrotorLabel = qtw.QLabel("A",self)
        mrotorSpinbox = qtw.QSpinBox(self)
        mrotorSpinbox.setRange(1,26)
        mrotorSpinbox.valueChanged.connect(lambda: valuechangem())

        rlayout.layout().addWidget(mrotorLabel,1,2)
        rlayout.layout().addWidget(mrotorSpinbox,2,2)

        rrotorLabel = qtw.QLabel("A",self)
        rrotorSpinbox = qtw.QSpinBox(self)
        rrotorSpinbox.setRange(1,26)
        rrotorSpinbox.valueChanged.connect(lambda: valuechanger())

        rlayout.layout().addWidget(rrotorLabel,1,3)
        rlayout.layout().addWidget(rrotorSpinbox,2,3)

        self.layout.addWidget(rlayout,1,1)

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
    