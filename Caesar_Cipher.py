"""
Encryption -> E(x) = (x+n) MOD 26

Decryption-> D(x)=(x-n) MOD 26

Where x is the is the letter in the message and n is the shifting value

"""
def EncryptedNumbers(Message:str,shift:int):
    transformed_message = transform(Message)
    encryptedNumbers = []
    for i in transformed_message:
        if isinstance(i, int):  # Only shift numeric characters
            encryptedNumbers.append((i + shift) % 26)
        else:
            encryptedNumbers.append(i)  # Preserve spaces and other characters
    return encryptedNumbers


def DecryptedNumbers(Message:str,shift:int):
    transformed_message = transform(Message)
    decryptedNum=[]
    for i in transformed_message:
        if isinstance(i, int):  # Only shift numeric characters
            decryptedNum.append((i - shift) % 26)
        else:
            decryptedNum.append(i)  # Preserve spaces and other characters
    return decryptedNum


def Decryption(Message: str, shift: int):
    Decrypted = []
    temp2 = DecryptedNumbers(Message, shift)
    numberChar2 = {
        0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f', 6: 'g', 7: 'h',
        8: 'i', 9: 'j', 10: 'k', 11: 'l', 12: 'm', 13: 'n', 14: 'o', 15: 'p',
        16: 'q', 17: 'r', 18: 's', 19: 't', 20: 'u', 21: 'v', 22: 'w', 23: 'x',
        24: 'y', 25: 'z' 
    }

    dec = ''
    for num in temp2:
        if num ==-1:
            dec+=" "
        elif num in numberChar2:
            dec += numberChar2[num]  # Directly add the character to the string
            
    return dec


def Encryption(Message:str,shift:int):
    Encrypted = []
    temp = EncryptedNumbers(Message,shift)
    numberChar = {
    0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f', 6: 'g', 7: 'h',
    8: 'i', 9: 'j', 10: 'k', 11: 'l', 12: 'm', 13: 'n', 14: 'o', 15: 'p',
    16: 'q', 17: 'r', 18: 's', 19: 't', 20: 'u', 21: 'v', 22: 'w', 23: 'x',
    24: 'y', 25: 'z'
    }
    enc=''
    for num in temp:
        if num in numberChar:
            Encrypted.append(str(numberChar[num]))  # Append the transformed value to the list
        else:
            Encrypted.append(num)

    for i in Encrypted: #to print the encypted message as a string
        enc=enc+i
    return enc



def transform(Message)->str:
# Dictionary containg all the alphabets
    charNumber={
        'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7,
        'i': 8, 'j': 9, 'k': 10, 'l': 11, 'm': 12, 'n': 13, 'o': 14, 'p': 15,
        'q': 16, 'r': 17, 's': 18, 't': 19, 'u': 20, 'v': 21, 'w': 22, 'x': 23,
        'y': 24, 'z': 25 
    
}
    transformed_message = []
# Iterate through each character in the input message
    for char in Message:
        if char ==" ":
            transformed_message.append(" ")
        elif char in charNumber:
            transformed_message.append(int(charNumber[char]))  # Append the transformed value to the list

        else:
            transformed_message.append(char)

    return transformed_message
# End of transform Function


Message = input("Enter your message: ").lower()
Shift = int(input("Enter the shifting value: "))
print(DecryptedNumbers(Message,Shift))
op = input("Choose waht do you wan \n E for encryption \n D for Decryption \n ").upper()

if op == 'E':
    print(Encryption(Message,Shift))

elif op == 'D':
    print(Decryption(Message,Shift))

else:
    print("Please enter a vaild operator")
