# Extended Vigenere Module
# This module consist of function for Extended Vigenere Algorithm
#
# Module Author: Justin Dermawan Ikhsan
# 18219095


def extendedVigenereEncrypt(plaintext,key):
    '''
    Encrypt given plaintext to ciphertext with standard 256 ASCII vigenere
    INPUT: cleaned plaintext and vigenere key
    OUTPUT: Vigenere-256 ciphertext
    '''
    cipher = ""
    for i in range(len(plaintext)):
        if ord(plaintext[i]) >=0 and ord(plaintext[i]) <=255:
            inChar = ord(plaintext[i])
            inKey = ord(key[i % len(key)])
            newChar = (inChar + inKey) % 256
            # print(f"{plaintext[i]} || {inChar} || {newChar} || {repr(chr(newChar))}")
            cipher +=chr(newChar)
        else:
            cipher += plaintext[i]
    return cipher

def extendedVigenereDecrypt(plaintext,key):
    '''
    Decrypt given ciphertext to plaintext with standard 256 ASCII vigenere
    INPUT: 256 ASCII Vigenere ciphertext and vigenere key
    OUTPUT: plaintext
    '''
    cipher = ""
    for i in range(len(plaintext)):
        if ord(plaintext[i]) >=0 and ord(plaintext[i]) <=255:
            inChar = ord(plaintext[i])
            inKey = ord(key[i % len(key)])
            newChar = (inChar - inKey) % 256
            cipher +=chr(newChar)
            # print(f"{repr(plaintext[i])} || {inChar} || {newChar} || {(chr(newChar))}")
        else:
            cipher += plaintext[i]
    return cipher

def encryptBinaryFile(filedir,key):
    '''
    Encrypt given binary file with 256 Extended ASCII Vigenere Cipher
    INPUT: file directory and Vigenere key
    OUTPUT: encrypted file at "cipher/files/encrypted.(extension)"
    '''
    ext = filedir.split("/")[-1].split(".")[-1]
    f = open(filedir,"rb")
    s = f.read()
    nf = extendedVigenereEncrypt(s.decode("ISO-8859-1") ,key)
    g = open(f"cipher/files/encrypted.{ext}","wb")
    g.write(bytes(nf,'ISO-8859-1'))
    g.close()

def decryptBinaryFile(filedir,key):
    '''
    Decrypt given binary file with 256 Extended ASCII Vigenere Cipher
    INPUT: file directory and Vigenere key
    OUTPUT: decrypted file at "cipher/files/decrypted.(extension)"
    '''
    ext = filedir.split("/")[-1].split(".")[-1]
    f = open(filedir,"rb")
    s = f.read()
    nf = extendedVigenereDecrypt(s.decode("ISO-8859-1") ,key)
    g = open(f"cipher/files/decrypted.{ext}","wb")
    g.write(bytes(nf,'ISO-8859-1'))
    g.close()

if __name__ == "__main__":
    plaintext = "Lorem ipsum dolor sit amet, consectetur adipiscing elit."
    key = "LEMON"
    # c = splitStringTo5Chars(repr(extendedVigenereEncrypt(plaintext,key)))
    # print(c)
    # print(splitStringTo5Chars(extendedVigenereDecrypt(c,key)))
    test= "ALoveA"
    print(test[:-1])
    print(test[:-1][1:])
    # encryptBinaryFile("cipher/files/aa.jpg",key)
    # decryptBinaryFile("cipher/files/encrypted.jpg",key)