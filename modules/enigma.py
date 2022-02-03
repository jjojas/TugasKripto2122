# Enigma Cipher dengan 3-rotor (26 huruf alfabet)
# Algoritma mesin Enigma I dengan 3-rotor (I,II,III) dan reflector(UKW-B)
# Asumsi: plugboard tidak diset dan Ring setting diatur pada 'A,A,A'
# Module Author: Bonaventura Bagas S
# 18219017

import string

AlphabetList = list(string.ascii_uppercase)
# rotor type I
rotor1 = list('EKMFLGDQVZNTOWYHXUSPAIBRCJ')
# rotor type II
rotor2 = list('AJDKSIRUXBLHWTMCQGZNPYFVOE')
# rotor type III
rotor3 = list('BDFHJLCPRTXVZNYEIWGAKMUSQO')
rotor1Notch = 'Q'
rotor2Notch = 'E'
rotor3Notch = 'V'
rotor1Position = 'A'
rotor2Position = 'A'
rotor3Position = 'A'
# UKW-B 
reflector = {'Y':'A','R':'B','U':'C','H':'D','Q':'E','S':'F','L':'G','D':'H','P':'I','X':'J','N':'K','G':'L','O':'M',
			'K':'N','M':'O','I':'P','E':'Q','B':'R','F':'S','Z':'T','C':'U','W':'V','V':'W','J':'X','A':'Y','T':'Z'}

def setEnigma(initial1, initial2, initial3):
	'''
	set each Enigma rotor an initial position
	'''
	global rotor1Position, rotor2Position, rotor3Position
	rotor1Position = initial1
	rotor2Position = initial2
	rotor3Position = initial3

def cleanText(text: str) -> str:
    cleanedText = ""
    text = text.upper().replace(" ", "")
    for char in text:
        if ord(char) >=65 and ord(char) <=90:
            cleanedText += char
    return cleanedText


def encryptAndDecrypt(plainText):
	'''
	Encrypt and decrypt text according to Enigma setting
	'''
	
	rotor1Char = rotor1Position
	rotor2Char = rotor2Position
	rotor3Char = rotor3Position

	isRotor2Rotate = False
	isRotor1Rotate = False

	cipherText = ""

	for char in plainText:
		if rotor3Char == rotor3Notch:
			isRotor2Rotate = True
			if rotor2Char == rotor2Notch:
				isRotor1Rotate = True

		rotor3Char = AlphabetList[(AlphabetList.index(rotor3Char) + 1) % 26]
		if (isRotor2Rotate):
			isRotor2Rotate = False
			rotor2Char = AlphabetList[(AlphabetList.index(rotor2Char) + 1) % 26]
		if (isRotor1Rotate):
			isRotor1Rotate = False
			rotor1Char = AlphabetList[(AlphabetList.index(rotor1Char) + 1) % 26]

		addIdx1 = AlphabetList.index(rotor1Char)
		addIdx2 = AlphabetList.index(rotor2Char)
		addIdx3 = AlphabetList.index(rotor3Char)

		tempLetter = char
		# Rotor3
		earlyPosition = (AlphabetList.index(tempLetter) + addIdx3) % 26
		tempLetter = AlphabetList[earlyPosition]
		endPosition = (rotor3.index(tempLetter) - addIdx3) % 26
		tempLetter = AlphabetList[endPosition]

		# Rotor2
		earlyPosition = (AlphabetList.index(tempLetter) + addIdx2) % 26
		tempLetter = AlphabetList[earlyPosition]
		endPosition = (rotor2.index(tempLetter) - addIdx2) % 26
		tempLetter = AlphabetList[endPosition]

		# Rotor1
		earlyPosition = (AlphabetList.index(tempLetter) + addIdx1) % 26
		tempLetter = AlphabetList[earlyPosition]
		endPosition = (rotor1.index(tempLetter) - addIdx1) % 26
		tempLetter = AlphabetList[endPosition]

		# Reflector
		tempLetter = reflector[tempLetter]

		# Rotor1
		earlyPosition = (AlphabetList.index(tempLetter) + addIdx1) % 26
		tempLetter = rotor1[earlyPosition]
		endPosition = (AlphabetList.index(tempLetter) - addIdx1) % 26
		tempLetter = AlphabetList[endPosition]

		# Rotor2
		earlyPosition = (AlphabetList.index(tempLetter) + addIdx2) % 26
		tempLetter = rotor2[earlyPosition]
		endPosition = (AlphabetList.index(tempLetter) - addIdx2) % 26
		tempLetter = AlphabetList[endPosition]

		# Rotor3
		earlyPosition = (AlphabetList.index(tempLetter) + addIdx3) % 26
		tempLetter = rotor3[earlyPosition]
		endPosition = (AlphabetList.index(tempLetter) - addIdx3) % 26
		result = AlphabetList[endPosition]

		cipherText += result

	return cipherText		

		
def textEncryptAndDecypt(text, initialPosition1, initialPosition2, initialPosition3):
	'''
	Encrypt and Decrypt input text with Enigma Cipher
	'''
	# set Enigma's rotor initial position
	setEnigma(initialPosition1, initialPosition2, initialPosition3)

	# clean input text
	text = cleanText(text)

	# encrypt or decrypt
	return encryptAndDecrypt(text)

def fileEncrypt(fileName, initialPosition1, initialPosition2, initialPosition3):
	'''
	Encrypt file input with Enigma Cipher
	'''
	# set Enigma's rotor initial position
	setEnigma(initialPosition1, initialPosition2, initialPosition3)

	with open(fileName, "rb") as file:
		# read all file data
		fileData = file.read()

	# convert fileData
	fileData = cleanText(fileData.decode('UTF-8'))

	# encrypt data
	encryptedData = encryptAndDecrypt(fileData)

	# write the decrypted file
	with open("cipher/text/encrypted_" + fileName.split("/")[-1], "wb") as file:
		file.write(bytes(encryptedData, 'UTF-8'))

def fileDecrypt(fileName, initialPosition1, initialPosition2, initialPosition3):
	'''
	Decrypt file input with Enigma Cipher
	'''
	# set Enigma's rotor initial position
	setEnigma(initialPosition1, initialPosition2, initialPosition3)

	with open(fileName, "rb") as file:
		# read all file data
		fileData = file.read()

	# convert fileData
	fileData = cleanText(fileData.decode('UTF-8'))

	# decrypted data
	decryptedData = encryptAndDecrypt(fileData)

	# write the decrypted file
	with open("cipher/text/decrypted_" + fileName.split("/")[-1], "wb") as file:
		file.write(bytes(decryptedData, 'UTF-8'))