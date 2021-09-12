alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""
print(logo)

def encrypt(text,shift):
    fword = ""
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    for i in text:
        if i.isalpha():
            pos = alphabet.index(i) + shift
            lim = len(alphabet) - 1
            if pos > lim:
                fpos = pos - lim-1
                fword += alphabet[fpos]
            else:
                fword += alphabet[pos]
        else:
            fword += i
    return fword
#print(encrypt(text,shift))


def decrypt(text,shift):
    fword = ""
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    for i in text:
        if i.isalpha():
            pos = alphabet.index(i) - shift
            fword += alphabet[pos]
        else:
            fword += i
    return fword
#print(decrypt(text,shift)) 
while True:  
    try:
    
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt or if you wanna stop the program type 'stop': ")
        if direction == "stop":
            print("Stopping............")
            break
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))

        if direction == "encode":
            print(encrypt(text,shift))
        elif direction == "decrypt":
            print(decrypt(text,shift)) 
        else:
            print("Enter a proper direction")
    except:
        print("Enter a proper shift variable!")
