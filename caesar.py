print("******************")
print("Welcome to Caesar Cipher")
print("******************")

def CaesarCipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            new_index = (ord(char) - start + shift) % 26
            shifted_char = chr(new_index + start)
            result += shifted_char
        else:
            result += char
    return result

choice = input("""
Do you want to
1. Encrypt a message
2. Decrypt a message
""")

if choice == '1':
    message = input("Enter the message to encrypt: ")
    shift = int(input("How many characters to shift (positive for encryption): "))
    encrypted_message = CaesarCipher(message, shift)
    print("The encrypted message is:", encrypted_message)

elif choice == '2':
    message = input("Enter the message to decrypt: ")
    shift = int(input("How many characters to shift (negative for decryption): "))
    decrypted_message = CaesarCipher(message, shift)
    print("The decrypted message is:", decrypted_message)

else:
    print("Invalid choice")