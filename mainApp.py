from hillcipher import Hill

def getVigenereKey(key:str, plainLen:int) -> str:
    keyLen = len(key)
    newKey=""
    i=0
    while True:
        if len(newKey)==plainLen:
            break
        if i>=keyLen:
            i=0
        newKey+=key[i]
        i+=1
    return newKey

def getCeasarKey(key:str) -> str:
    cipher = ""
    for index in range(len(key)):
        cipher += chr((ord(key[index])+index) % 95)
 
    return cipher

def getHillKey(key:str) -> str:
    return Hill.hill_cipher(plain_text=key)

def VignereCipherEncrypt(plaintext:str, key:str)->str:
    new=""
    j=0
    for i in plaintext:
        if len(key)==j:
            j=0
        new+=chr(ord(i)+ord(key[j]))
        j+=1
    return new

def VigenereCipherDecrypt(text:str, key:str)->str:
    old=""
    j=0
    for i in text:
        if len(key)==j:
            j=0
        old+=chr(ord(i)-ord(key[j]))
        j+=1
    return old

def main():
    """
    This is the driver function of the program. It takes user input and then runs the program to give you encrypted or decrypted text.
    """
    # Taking User Inputs
    
    plaintext = input("Enter your message: ")
    key = input("Enter your key: ")
    
    plainLen = len(plaintext)
    # Getting the Vigenere Key
    newKey = getVigenereKey(key, plainLen)
    # Running newKey through Ceasar Ciper
    ceasarKey = getCeasarKey(newKey)
    # Running ceasarKey through Hill's Cipher
    actualKey = getHillKey(ceasarKey)
    # Now we have got the actual key and we will run this along with the plain text through Vigenere Cipher 
    cipherText = VignereCipherEncrypt(plaintext,actualKey)
    print("The Cipher Text is : ", cipherText)

    # Decrypting the Cipher Text for confirmation using the actual key
    plainText = VigenereCipherDecrypt(cipherText, actualKey)
    print("The Plain Text is: ", plainText)

if __name__ == "__main__":
    main()