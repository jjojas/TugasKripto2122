#One-time pad (26 huruf alfabet)

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


# print(encrypt("nantimalamsayatunggukamudidepanwarungkopi".upper(), "gtrskncvbrwpoatqljfmxtrpjsrzolfhtbmaedpvy".upper()))
# print(decrypt("TTELSZCGBDOPMAMKYPLGHTDJMAUDDLSDTSGNKNDKG", "gtrskncvbrwpoatqljfmxtrpjsrzolfhtbmaedpvy".upper()))
# print(textEncrypt("nantimalamsayatunggukamudidepanwarungkopi"))
# print(textDecrypt("WFOEIWWUETHFGNDYWNLHCJZPVLRJLEBMPNYDKXQCH"))
# print(textDecrypt("ZXWAQTBBUPAAOIPBRUVQBUGLEHEQSVAXIHQRVVNBF"))
# print(textEncrypt("ada cerita"))
print(textDecrypt("CEVAWYICS"))