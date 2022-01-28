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
            pass
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
            pass
    return cipher

a = vigenere_encrypt("AYAM KALASAN ENAK SEKALI SOBAT","LEMON")
print(a)
b = vigenere_decrypt(a,"LEMON")
print(b)