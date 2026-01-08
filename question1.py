shift1 = int(input("Enter shift-1: "))
shift2 = int(input("Enter shift-2: "))
text = "abc m n xyz ABC M N XYZ"

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
    
def decrypt_rules(char):
    if 'a' <= char <= 'm':
        return chr((ord(char) - ord('a') - (shift1 * shift2)) % 13 + ord('a'))

    elif 'n' <= char <= 'z':
        return chr((ord(char) - ord('n') + (shift1 + shift2)) % 13 + ord('n'))

    elif 'A' <= char <= 'M':
        return chr((ord(char) - ord('A') + shift1) % 13 + ord('A'))

    elif 'N' <= char <= 'Z':
        return chr((ord(char) - ord('N') - (shift2 ** 2)) % 13 + ord('N'))

    else:
        return char

def encryption(text):
    encrypted_text = ""
    
    for char in text:
        encrypted_text += encrypt_rules(char)

    print("File encrypted successfully.")
    print('encrypted text: ',encrypted_text)
    return encrypted_text

new_text = encryption(text)
print("New Text: ",new_text)

def decryption(new_text):
    encrypted_text = new_text
    decrypted_text = ""
    
    for char in encrypted_text:
        decrypted_text += decrypt_rules(char)

    print("File decrypted successfully.")
    print('Decryption Text: ',decrypted_text)

decryption(new_text)
print('original text: ',text)

