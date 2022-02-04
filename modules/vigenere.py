# Vigenere Module
# This module consist of function for Vigenere Algorithm
#
# Module Author: Justin Dermawan Ikhsan
# 18219095

def cleanText(text):
    '''
    Clean given text for vigenere cipher
    INPUT: any given string
    OUTPUT: cleaned string (removed char, transform to uppercase)
    '''
    cleanedText = ""
    text = text.upper().replace(" ", "")
    for char in text:
        if ord(char) >=65 and ord(char) <=90:
            cleanedText += char
    return cleanedText

def vigenereEncrypt(plaintext,key):
    '''
    Encrypt given plaintext to ciphertext with standard 26 ASCII vigenere
    INPUT: cleaned plaintext and vigenere key
    OUTPUT: Vigenere-26 ciphertext
    '''
    cipher = ""
    plaintext = cleanText(plaintext)
    key = cleanText(key)
    for i in range(len(plaintext)):
        if ord(plaintext[i]) >=65 and ord(plaintext[i]) <=90:
            inChar = ord(plaintext[i]) - 65
            inKey = ord(key[i % len(key)]) - 65
            newChar = (inChar + inKey) % 26
            cipher +=chr(newChar+65)
        else:
            cipher += plaintext[i]
    return cipher

def vigenereDecrypt(ciphertext,key):
    '''
    Decrypt given ciphertext to plaintext with standard 26 ASCII vigenere
    INPUT: 26 ASCII Vigenere ciphertext and vigenere key
    OUTPUT: plaintext
    '''
    plain = ""
    ciphertext = cleanText(ciphertext)
    key = cleanText(key)
    for i in range(len(ciphertext)):
        if ord(ciphertext[i]) >=65 and ord(ciphertext[i]) <=90:
            inChar = ord(ciphertext[i]) - 65
            inKey = ord(key[i % len(key)]) - 65
            newChar = (inChar - inKey) % 26
            plain +=chr(newChar+65)
        else:
            plain += ciphertext[i]
    return plain

def splitStringTo5Chars(text):
    '''
    Split given string by 5 characthers
    INPUT: string
    OUTPUT: splitted string
    '''
    txt = ""
    ars = [ text[i:i+5] for i in range(0, len(text), 5)]
    for ar in ars:
        txt += ar + " "
    return txt

def encryptTextFile(filedir,key):
    '''
    Open plaintext and encrypt it with 26 vigenere cipher
    INPUT: filedir
    OUTPUT: ciphered text
    '''
    f = open(filedir,"r+")
    c = f.read()
    f.close()

    s = open(f"cipher/text/encrypted_{filedir.split('/')[-1]}","w+")
    s.write(vigenereEncrypt(c,key))
    s.close()

def decryptTextFile(filedir,key):
    '''
    Open ciphertext text file and decrypt it with 26 vigenere cipher
    INPUT: filedir
    OUTPUT: plaintext files
    '''
    f = open(filedir,"r+")
    c = f.read()
    f.close()

    s = open(f"cipher/text/decrypted_{filedir.split('/')[-1]}","w+")
    s.write(vigenereDecrypt(c,key))
    s.close()

def saveCipherToTextfile(content,filename):
    '''
    Save ciphertext to text file
    INPUT: string
    OUTPUT: splitted string
    '''
    f = open(f"cipher/text/{filename}.txt","w+")
    f.write(content)
    f.close()

if __name__ == "__main__":
    plaintext = "Lorem ipsum dolor sit amet, consectetur adipiscing elit."
    key = "LEMON"
    # vigenereCipher = vigenereEncrypt(plaintext,key)
    # vigenereDecipher = vigenereDecrypt(vigenereCipher,key)
    # vigenereExCipher = extendedVigenereEncrypt(plaintext,key)
    # vigenereExDecipher = extendedVigenereDecrypt(vigenereExCipher,key)
    # print(f"VC: {splitStringTo5Chars(vigenereCipher)}\nVD: {splitStringTo5Chars(vigenereDecipher)}")
    # print(f"EVC: {repr(vigenereExCipher)}\nDVC: {splitStringTo5Chars(vigenereExDecipher)}")
    # encryptBinaryFile("cipher/files/aa.jpg",key)
    s = encryptTextFile("cipher/text/test.txt",key)
    saveCipherToTextfile(s,"encrypted")
    d = decryptTextFile("cipher/text/encrypted.txt",key)
    saveCipherToTextfile(d,"decrypted")
    # decryptBinaryFile("cipher/files/encrypted.jpg")
    # decryptBinaryFile("")
    # saveCipherToTextfile(splitStringTo5Chars(vigenereCipher,"Vichip"))