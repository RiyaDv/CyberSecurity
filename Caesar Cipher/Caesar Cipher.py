def encrypt(text, shift):
    result = ""

    # Traverse text
    for i in range(len(text)):
        char = text[i]

        # Encrypt uppercase characters
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        # Encrypt lowercase characters
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += char

    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

def main():
    while True:
        choice = input("Enter \n 1. Encrypt \n 2. Decrypt \n q. Quit \n Enter Your Choice:")

        if choice == '1':
            text = input("\n Enter the message to encrypt: ")
            shift = int(input("Enter the shift value: "))
            encrypted_text = encrypt(text, shift)
            print(f"\n Encrypted message: {encrypted_text}\n")

        elif choice == '2':
            text = input("\n Enter the message to decrypt: ")
            shift = int(input("\n  Enter the shift value: "))
            decrypted_text = decrypt(text, shift)
            print(f"\n Decrypted message: {decrypted_text}\n")

        elif choice == 'q':
            print("\n Exiting the program.")
            break

        else:
            print("\n Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()
