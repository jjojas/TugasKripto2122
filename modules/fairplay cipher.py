from msilib.schema import Error
import string
from turtle import pen

AlphabetList = list(string.ascii_lowercase)

def toLowerCase(string: str) -> str:
    '''
    set string to lower case
    '''
    return string.lower()


def removeUnrecognizedChar(string: str) -> str:
    '''
    remove all unrecognized chars or punctuations such as (space), .(period), ,(coma), etc
    '''
    return ''.join(e for e in string if e in AlphabetList)


def removeDuplicateChar(string: str) -> str:
    '''
    remove all duplicates and 'j' from string and keep the order of characters
    '''
    result = ""
    for char in string:
        if(char in result or char == 'j'):
            pass
        else:
            result+=char
    return result


def generateKeySquare(keyStr: str):
    '''
    generate a 5x5 key square from an acceptable key string
    '''
    keySquare = [['i' for i in range (5)] for j in range (5)]

    for char in AlphabetList:
        if (char in keyStr or char == 'j'):
            pass
        else:
            keyStr+=char

    for i in range (len(keySquare)):
        for j in range (len(keySquare[i])):
            keySquare[i][j] = keyStr[i*len(keySquare[0])+j]
    
    return keySquare


def convertPlainTextToBigrams(plainText: str):
    '''
    convert a PlainText to acceptable Bigrams
    '''
    #1.ganti huruf 'j' ke 'i'
    #2.bagi jadi bigram
    #3.add 'x' kalo ada pasangan yang sama
    #4.add 'x' kalo ganjil
    plainText = plainText.replace('j', 'i')

    i = 0
    while i < len(plainText):
        if i != len(plainText)-1:
            if plainText[i] == plainText[i+1]:
                plainText = plainText[:i+1] + 'x' + plainText[i+1:]
        i+=2

    if len(plainText) % 2 != 0:
        plainText += 'x'
    
    return plainText 


def findCharLocation(char1, char2, keySquare):
    '''
    find the index of char in Key Square
    '''
    indexOfChar1 = []
    indexOfChar2 = []

    for i in range (len(keySquare)):
        for j in range (len(keySquare[i])):
            if keySquare[i][j] == char1:
                indexOfChar1.append(i)
                indexOfChar1.append(j)
            elif keySquare[i][j] == char2:
                indexOfChar2.append(i)
                indexOfChar2.append(j)
    
    return indexOfChar1, indexOfChar2


def mod5(x: int):
    if x<0:
        x+=5
    return x%5


def encrypt(plainText: str, keySquare):
    '''
    receive an acceptable plainText, return encrypted text
    '''
    #1.find char the location in the square
    #2.get the cipher char
    #3.assemble the cipher

    cipherText = []

    i = 0
    while i < len(plainText):
        index1, index2 = findCharLocation(plainText[i], plainText[i+1], keySquare)

        if index1[0] == index2[0]:
            cipherIdxCol1 = mod5(index1[1]+1)
            cipherIdxRow1 = index1[0]
            cipherIdxCol2 = mod5(index2[1]+1)
            cipherIdxRow2 = index2[0]

        elif index1[1] == index2[1]:
            cipherIdxCol1 = index1[1]
            cipherIdxRow1 = mod5(index1[0]+1)
            cipherIdxCol2 = index2[1]
            cipherIdxRow2 = mod5(index2[0]+1)

        else:
            cipherIdxCol1 = index2[1]
            cipherIdxRow1 = index1[0]
            cipherIdxCol2 = index1[1]
            cipherIdxRow2 = index2[0]

        cipherText.append(keySquare[cipherIdxRow1][cipherIdxCol1])
        cipherText.append(keySquare[cipherIdxRow2][cipherIdxCol2])
        i+=2

    return ''.join(cipherText)


def textEncrypt(plainText: str, plainKey: str):
    '''
    Encrypt a plainText with keySquare
    '''
    #generate keySquare
    keyString = removeUnrecognizedChar(plainKey.lower())
    keyString = removeDuplicateChar(keyString)
    keySquare = generateKeySquare(keyString)

    #plain text
    plainText = removeUnrecognizedChar(plainText.lower())
    convertedPlainText = convertPlainTextToBigrams(plainText)

    #encript
    print(encrypt(convertedPlainText, keySquare))


def decrypt(cipherText: str, keySquare):
    '''
    receive an acceptable cipherText, return decrypted text
    '''
    #1.find char the location in the square
    #2.get the cipher char
    #3.assemble the cipher

    plainText = []

    i = 0
    while i < len(cipherText):
        index1, index2 = findCharLocation(cipherText[i], cipherText[i+1], keySquare)

        if index1[0] == index2[0]:
            plainIdxCol1 = mod5(index1[1]-1)
            plainIdxRow1 = index1[0]
            plainIdxCol2 = mod5(index2[1]-1)
            plainIdxRow2 = index2[0]

        elif index1[1] == index2[1]:
            plainIdxCol1 = index1[1]
            plainIdxRow1 = mod5(index1[0]-1)
            plainIdxCol2 = index2[1]
            plainIdxRow2 = mod5(index2[0]-1)

        else:
            plainIdxCol1 = index2[1]
            plainIdxRow1 = index1[0]
            plainIdxCol2 = index1[1]
            plainIdxRow2 = index2[0]

        plainText.append(keySquare[plainIdxRow1][plainIdxCol1])
        plainText.append(keySquare[plainIdxRow2][plainIdxCol2])
        i+=2

    return ''.join(plainText).replace('x', '')


def textDecrypt(cipherText: str, plainKey: str):
    '''
    Encrypt a plainText with keySquare
    '''
    #generate keySquare
    keyString = removeUnrecognizedChar(plainKey.lower())
    keyString = removeDuplicateChar(keyString)
    keySquare = generateKeySquare(keyString)

    #cipher text
    cipherText = removeUnrecognizedChar(cipherText.lower())
    if len(cipherText) % 2 != 0:
        raise TypeError("Odd-length string")

    #decrypt
    print(decrypt(cipherText, keySquare))


def fileEncrypt(fileName, plainKey: str):
    '''
    Given a filename (str), it encrypt the file and write a new encrypted file
    '''
    # generate keySquare
    keyString = removeUnrecognizedChar(plainKey.lower())
    keyString = removeDuplicateChar(keyString)
    keySquare = generateKeySquare(keyString)

    with open(fileName, "rb") as file:
        # read all file data
        fileData = file.read()

    # convert fileData
    fileData = removeUnrecognizedChar(fileData.decode('UTF-8').lower())
    convertedFileData = convertPlainTextToBigrams(fileData)

    # encrypt data
    encryptedData = encrypt(convertedFileData, keySquare)
    
    # write the encrypted file
    with open("encrypted_" + fileName, "wb") as file:
        file.write(bytes(encryptedData, 'UTF-8'))


def fileDecrypt(fileName, plainKey: str):
    '''
    Given a filename (str), it decrypt the file and write a new decrypted file
    '''
    #generate keySquare
    keyString = removeUnrecognizedChar(plainKey.lower())
    keyString = removeDuplicateChar(keyString)
    keySquare = generateKeySquare(keyString)

    with open(fileName, "rb") as file:
        # read all file data
        fileData = file.read()

    # convert fileData
    fileData = removeUnrecognizedChar(fileData.decode('UTF-8').lower())
    convertedFileData = convertPlainTextToBigrams(fileData)

    # decrypted data
    decryptedData = decrypt(convertedFileData, keySquare)
    
    # write the decrypted file
    with open("decrypted_" + fileName, "wb") as file:
        file.write(bytes(decryptedData, 'UTF-8'))

# sting= "jalan ganesha sepuluh"
# print(toLowerCase(sting))
# clear_str = removeUnrecognizedChar(sting.lower())
# print(clear_str)
# clear_str = removeDuplicateChar(clear_str)
# print(clear_str)
# key = generateKeySquare(clear_str)

# # plain = "gemuiibunantimalam"
# # cvt_plain = convertPlainTextToBigrams(plain)

# # print(key)
# # print(findCharLocation('q','x',key))

# # print(encrypt(cvt_plain, key))

# # textEncrypt("jjjjjjj", "jalan ganesha sepuluh")

# print(decrypt("zbrsfykupglgrkvsnlqv", key))

# textDecrypt("zbrsfykupglgrkvsnlq", "jalan ganesha sepuluh")

# fileEncrypt("test.txt", "jalan ganesha sepuluh")

# fileEncrypt("finance.csv", "jalan ganesha sepuluh")

fileDecrypt("encrypted_test.txt", "jalan ganesha sepuluh")