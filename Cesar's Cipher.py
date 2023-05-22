__author__ = 'Nicolas de Moura'
__date__ = '30/03/2022'
__version__ = 1.0

def Cipher():
    print("""           
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
""")
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k'
    , 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x'
    , 'y', 'z']
    command = str(input("Type 'decrypt' or 'encrypt': ")).lower()
    text = str(input("Enter a text: ")).lower()
    shift = int(input("Enter a shift amount: "))
    if shift > 26:
        shift = shift % 26
        if shift > 26:
            shift = 26
    if shift < (-26):
        shift = (shift * (-1)) % 26
    elif shift < 0 and shift > (-26):
        shift = shift * (-1)
    cipher = ''
    try:
        for letter in text:
            if letter in alphabet:
                position = alphabet.index(letter)
                if command == "encrypt":
                    new_position = position + shift
                    if new_position > 26:
                        new_position = new_position - 26
                elif command == "decrypt":
                    new_position = position - shift
                    if new_position < 0:
                        new_position = 26 + (new_position)
                cipher += alphabet[new_position]
            else:
                cipher += letter
        print(f"Your Encrypted/Decrypted text is {cipher}")
    except UnboundLocalError:
        print(f"{command} isn't recognized as a command")
if __name__ == "__main__":
    while True:
        Cipher()
        if input("Type any keyword to continue or enter to exit: ") == "":
            break
