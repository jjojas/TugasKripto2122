# One-time pad Module (26 alphabet)
# Module Author: Bonaventura Bagas S
# 18219017

def cleanText(text: str) -> str:
    cleanedText = ""
    text = text.upper().replace(" ", "")
    for char in text:
        if ord(char) >=65 and ord(char) <=90:
            cleanedText += char
    return cleanedText

#Encrypt
def generateKey(plainTextLength: int) -> str:
    '''
    generate key from key.txt which has the same length with plaintText
    '''
    with open("modules/otp_file/key.txt", "r") as inFile:
        # read all file data
        keyData = inFile.read()
        keyStr = keyData[:plainTextLength]

    # write the file
    with open("modules/otp_file/key.txt", "w") as outFile:
        temp = keyData[plainTextLength:]
        outFile.write(temp)

    return keyStr


def saveChiperandUsedKey(cipherText: str, key: str):
    # Append cipherText
    with open("modules/otp_file/cipher.txt", "a") as file:
        # Append cipherText at the end of file
        file.write(str(len(cipherText))+cipherText)

    with open("modules/otp_file/usedKey.txt", "a") as file:
        # Append cipherText at the end of file
        file.write(str(len(key))+key)

def encrypt(plainText, key: str):
    cipherText = ""

    for i in range(len(plainText)):
        charText = plainText[i]
        charKey = key[i]

        # Encrypt characters in plain text
        cipherText += chr((ord(charText)-65 + ord(charKey)-65) % 26 + 65)
        
    return cipherText

def textEncrypt(plainText: str) -> str:
    # clean plainText
    plainText = cleanText(plainText)

    # generate key
    key = generateKey(len(plainText))

    # encrypt plainText
    cipherText = encrypt(plainText, key)

    # save cipher and used Key
    saveChiperandUsedKey(cipherText, key)

    return cipherText

def fileEncrypt(fileName):
    '''
    Given a fileName (str), it decrypt the file and write a new decrypted file
    '''
    with open(fileName, "rb") as file:
        # read all file data
        fileData = file.read()

    # convert fileData
    fileData = cleanText(fileData.decode('UTF-8'))

    # generate key
    key = generateKey(len(fileData))

    # encrypt data
    encryptedData = encrypt(fileData, key)
    
    # write the decrypted file
    with open("cipher/text/encrypted_" + fileName.split("/")[-1], "wb") as file:
        file.write(bytes(encryptedData, 'UTF-8'))


#Decrypt
def getKey(cipherText: str):
    savedCipher = str(len(cipherText))+cipherText
    try:
        with open("modules/otp_file/cipher.txt", "r") as file:
            data = file.read()
            idx = data.index(savedCipher)
    except (ValueError):
        raise ValueError("CipherText not found")

    with open("modules/otp_file/usedKey.txt", "r") as file:
        data = file.read()
        key = data[idx:idx+len(savedCipher)]

    return cleanText(key)

def decrypt(cipherText, key: str):
    plainText = ""

    for i in range(len(cipherText)):
        charText = cipherText[i]
        charKey = key[i]

        # Encrypt characters in plain text
        plainText += chr((ord(charText)-65 - ord(charKey)-65) % 26 + 65)
        
    return plainText

def textDecrypt(cipherText: str) -> str:
    # clean cipherText
    cipherText = cleanText(cipherText)

    # check if key for cipherText exists
    key = getKey(cipherText)

    # decrypt cipherText
    plainText = decrypt(cipherText, key)

    return plainText

def fileDecrypt(fileName):
    '''
    Given a fileName (str), it decrypt the file and write a new decrypted file
    '''
    with open(fileName, "rb") as file:
        # read all file data
        fileData = file.read()
    
    # convert fileData
    fileData = cleanText(fileData.decode('UTF-8'))

    # check if key for cipherText exists
    key = getKey(fileData)

    # decrypted data
    decryptedData = decrypt(fileData, key)
    
    # write the decrypted file
    with open("cipher/text/decrypted_" + fileName.split("/")[-1], "wb") as file:
        file.write(bytes(decryptedData, 'UTF-8'))

# print(encrypt("nantimalamsayatunggukamudidepanwarungkopi".upper(), "gtrskncvbrwpoatqljfmxtrpjsrzolfhtbmaedpvy".upper()))
# print(decrypt("TTELSZCGBDOPMAMKYPLGHTDJMAUDDLSDTSGNKNDKG", "gtrskncvbrwpoatqljfmxtrpjsrzolfhtbmaedpvy".upper()))
# print(textEncrypt("nantimalamsayatunggukamudidepanwarungkopi"))
# print(textDecrypt("WFOEIWWUETHFGNDYWNLHCJZPVLRJLEBMPNYDKXQCH"))
# print(textDecrypt("ZXWAQTBBUPAAOIPBRUVQBUGLEHEQSVAXIHQRVVNBF"))
# print(textEncrypt("ada cerita"))
# print(textDecrypt("CEVAWYICS"))