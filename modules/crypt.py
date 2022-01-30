def vigenere_encrypt(plaintext,key):
    cipher = ""
    plaintext = plaintext.upper().replace(" ", "")
    key = key.upper().replace(" ", "")
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
    plaintext = plaintext.upper().replace(" ", "")
    key = key.upper().replace(" ", "")
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
    plaintext = plaintext.upper().replace(" ", "")
    key = key.upper().replace(" ", "")
    for i in range(len(plaintext)):
        if ord(plaintext[i]) >=0 and ord(plaintext[i]) <=255:
            inChar = ord(plaintext[i])
            inKey = ord(key[i % len(key)])
            newChar = (inChar + inKey) % 256
            cipher +=chr(newChar)
            # print(f"{inChar} - {newChar}")
            # print(f"{chr(inChar)} - {chr(newChar)}")
        else:
            cipher += plaintext[i]
    return cipher

def extended_vigenere_decrypt(plaintext,key):
    cipher = ""
    plaintext = plaintext.upper().replace(" ", "")
    key = key.upper().replace(" ", "")
    for i in range(len(plaintext)):
        if ord(plaintext[i]) >=0 and ord(plaintext[i]) <=255:
            inChar = ord(plaintext[i])
            inKey = ord(key[i % len(key)])
            newChar = (inChar - inKey) % 256
            cipher +=chr(newChar)
        else:
            cipher += plaintext[i]
    return cipher

if __name__ == "__main__":
    plaintext = "Aku suka makan ayam, dia suka makan somay!"
    key = "LEMON"
    vigenereCipher = vigenere_encrypt(plaintext,key)
    vigenereDecipher = vigenere_decrypt(vigenereCipher,key)
    vigenereExCipher = extended_vigenere_encrypt(plaintext,key)
    vigenereExDecipher = extended_vigenere_decrypt(vigenereExCipher,key)
    print(f"VC: {vigenereCipher}\nVD: {vigenereDecipher}")
    print(f"EVC: {repr(vigenereExCipher)}\nDVC: {vigenereDecipher}")