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
    s = f.read()
    f.close()

    return splitStringTo5Chars(vigenereEncrypt(s,key)) 

def decryptTextFile(filedir,key):
    '''
    Open ciphertext text file and decrypt it with 26 vigenere cipher
    INPUT: filedir
    OUTPUT: plaintext files
    '''
    f = open(filedir,"r+")
    s = f.read()
    f.close()
    return splitStringTo5Chars(vigenereDecrypt(s,key))

def saveCipherToTextfile(content,filename):
    '''
    Save ciphertext to text file
    INPUT: string
    OUTPUT: splitted string
    '''
    f = open(f"../cipher/text/{filename}.txt","w+")
    f.write(content)
    f.close()

def encryptBinaryFile(filedir,key):
    '''
    Encrypt given binary file with 256 Extended ASCII Vigenere Cipher
    INPUT: file directory and Vigenere key
    OUTPUT: encrypted file at "../cipher/files/encrypted.(extension)"
    '''
    ext = filedir.split("/")[-1].split(".")[-1]
    f = open(filedir,"rb")
    s = f.read()
    nf = extendedVigenereEncrypt(s.decode("ISO-8859-1") ,key)
    g = open(f"../cipher/files/encrypted.{ext}","wb")
    g.write(bytes(nf,'ISO-8859-1'))
    g.close()

def decryptBinaryFile(filedir,key):
    '''
    Decrypt given binary file with 256 Extended ASCII Vigenere Cipher
    INPUT: file directory and Vigenere key
    OUTPUT: decrypted file at "../cipher/files/decrypted.(extension)"
    '''
    ext = filedir.split("/")[-1].split(".")[-1]
    f = open(filedir,"rb")
    s = f.read()
    nf = extendedVigenereDecrypt(s.decode("ISO-8859-1") ,key)
    g = open(f"../cipher/files/decrypted.{ext}","wb")
    g.write(bytes(nf,'ISO-8859-1'))
    g.close()

if __name__ == "__main__":
    plaintext = "Lorem ipsum dolor sit amet, consectetur adipiscing elit."
    key = "LEMON"
    # vigenereCipher = vigenereEncrypt(plaintext,key)
    # vigenereDecipher = vigenereDecrypt(vigenereCipher,key)
    # vigenereExCipher = extendedVigenereEncrypt(plaintext,key)
    # vigenereExDecipher = extendedVigenereDecrypt(vigenereExCipher,key)
    # print(f"VC: {splitStringTo5Chars(vigenereCipher)}\nVD: {splitStringTo5Chars(vigenereDecipher)}")
    # print(f"EVC: {repr(vigenereExCipher)}\nDVC: {splitStringTo5Chars(vigenereExDecipher)}")
    # encryptBinaryFile("../cipher/files/aa.jpg",key)
    s = encryptTextFile("../cipher/text/test.txt",key)
    saveCipherToTextfile(s,"encrypted")
    d = decryptTextFile("../cipher/text/encrypted.txt",key)
    saveCipherToTextfile(d,"decrypted")
    # decryptBinaryFile("../cipher/files/encrypted.jpg")
    # decryptBinaryFile("")
    # saveCipherToTextfile(splitStringTo5Chars(vigenereCipher,"Vichip"))