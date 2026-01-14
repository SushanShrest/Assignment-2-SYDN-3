# Take shift values from user. 
shift1 = int(input("Enter shift-1: "))
shift2 = int(input("Enter shift-2: "))

# Encryption rules for each character.
def encrypt_rules(char):
    # Lowercase a-m
    if 'a' <= char <= 'm':
        return chr((ord(char) - ord('a') + (shift1 * shift2)) % 13 + ord('a'))

    # Lowercase n-z
    elif 'n' <= char <= 'z':
        return chr((ord(char) - ord('n') - (shift1 + shift2)) % 13 + ord('n'))

    # Uppercase A-M
    elif 'A' <= char <= 'M':
        return chr((ord(char) - ord('A') - shift1) % 13 + ord('A'))

    # Uppercase N-Z
    elif 'N' <= char <= 'Z':
        return chr((ord(char) - ord('N') + (shift2 ** 2)) % 13 + ord('N'))

    # Others
    else:
        return char

# Decryption rules for each character.
def decrypt_rules(char):
    # Reverse Lowercase a-m
    if 'a' <= char <= 'm':
        return chr((ord(char) - ord('a') - (shift1 * shift2)) % 13 + ord('a'))

    # Reverse Lowercase n-z
    elif 'n' <= char <= 'z':
        return chr((ord(char) - ord('n') + (shift1 + shift2)) % 13 + ord('n'))

    # Reverse Uppercase A-M
    elif 'A' <= char <= 'M':
        return chr((ord(char) - ord('A') + shift1) % 13 + ord('A'))

    # Reverse Uppercase N-Z
    elif 'N' <= char <= 'Z':
        return chr((ord(char) - ord('N') - (shift2 ** 2)) % 13 + ord('N'))

    # Others
    else:
        return char

# Encrypt file content
def encryption():
    with open("raw_text.txt", "r") as file:
        text = file.read()

    encrypted_text = ""
    
    for char in text:
        encrypted_text += encrypt_rules(char)
    
    with open("encrypted_text.txt", "w") as file:
        file.write(encrypted_text)

    print("File encrypted successfully.")

# Decrypt file content
def decryption():
    with open("encrypted_text.txt", "r") as file:
        encrypted_text = file.read()

    decrypted_text = ""
    
    for char in encrypted_text:
        decrypted_text += decrypt_rules(char)
    
    with open("decrypted_text.txt", "w") as file:
        file.write(decrypted_text)

    print("File decrypted successfully.")

# Verify decrypted file matches original
def verify():
    with open("raw_text.txt", "r") as file1, open("decrypted_text.txt", "r") as file2:
        if file1.read() == file2.read():
            print("Verification Successful: Content matches.")
        else:
            print("Verification Failed: Content does not match.")

# Run all functions.
encryption()
decryption()
verify()
