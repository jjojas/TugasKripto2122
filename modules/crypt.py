from pydoc import plain


def cleanText(text):
    '''
    Clean given text 
    '''
    cleanedText = ""
    text = text.upper().replace(" ", "")
    for char in text:
        if ord(char) >=65 and ord(char) <=90:
            cleanedText += char
    return cleanedText

def vigenere_encrypt(plaintext,key):
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

def vigenere_decrypt(plaintext,key):
    cipher = ""
    plaintext = cleanText(plaintext)
    key = cleanText(key)
    for i in range(len(plaintext)):
        if ord(plaintext[i]) >=65 and ord(plaintext[i]) <=90:
            inChar = ord(plaintext[i]) - 65
            inKey = ord(key[i % len(key)]) - 65
            newChar = (inChar - inKey) % 26
            cipher +=chr(newChar+65)
        else:
            cipher += plaintext[i]
    return cipher

def extended_vigenere_encrypt(plaintext,key):
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

def extended_vigenere_decrypt(plaintext,key):
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

def splitify(text):
    txt = ""
    ars = [ text[i:i+5] for i in range(0, len(text), 5)]
    for ar in ars:
        txt += ar + " "
    return txt

if __name__ == "__main__":
    plaintext = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. "
    key = "LEMON"
    vigenereCipher = vigenere_encrypt(plaintext,key)
    vigenereDecipher = vigenere_decrypt(vigenereCipher,key)
    vigenereExCipher = extended_vigenere_encrypt(plaintext,key)
    vigenereExDecipher = extended_vigenere_decrypt(vigenereExCipher,key)
    print(f"VC: {splitify(vigenereCipher)}\nVD: {splitify(vigenereDecipher)}")
    print(f"EVC: {repr(vigenereExCipher)}\nDVC: {splitify(vigenereExDecipher)}")