shift1 = int(input("Enter shift-1: "))
shift2 = int(input("Enter shift-2: "))

def encrypt_rules(char):
    if 'a' <= char <= 'm':
        return chr((ord(char) - ord('a') + (shift1 * shift2)) % 13 + ord('a'))

    elif 'n' <= char <= 'z':
        return chr((ord(char) - ord('n') - (shift1 + shift2)) % 13 + ord('n'))

    elif 'A' <= char <= 'M':
        return chr((ord(char) - ord('A') - shift1) % 13 + ord('A'))

    elif 'N' <= char <= 'Z':
        return chr((ord(char) - ord('N') + (shift2 ** 2)) % 13 + ord('N'))

    else:
        return char

def encryption():
    text = "abc m n xyz ABC M N XYZ"
    encrypted_text = ""
    
    for char in text:
        encrypted_text += encrypt_rules(char)

    print("File encrypted successfully.")
    print(encrypted_text)

encryption()

