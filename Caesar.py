def caeserKey(plain:str):
    cipher = ""
    for index in range(len(plain)):
        cipher += chr((ord(plain[index])+index) % 95)
 
    return cipher
 
if __name__=="__main__":
    plain = input("Enter the plain text: ")
    # key = int(input("Enter the key(a number): "))
    crypt = caeserKey(plain)
 
    print("Encrypted: "+crypt)

