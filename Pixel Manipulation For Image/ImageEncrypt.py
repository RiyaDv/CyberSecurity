from PIL import Image
import numpy as np

def encrypt_image(image_path, key):
    image = Image.open(image_path)
    image_data = np.array(image)

    encrypted_data = (image_data + key) % 256  # Basic operation for encryption

    encrypted_image = Image.fromarray(encrypted_data.astype(np.uint8))
    encrypted_image.save('encrypted_image.png')
    print("Image encrypted and saved as 'encrypted_image.png'")
    encrypted_image.show()  # Open the encrypted image

def decrypt_image(image_path, key):
    image = Image.open(image_path)
    image_data = np.array(image)

    decrypted_data = (image_data - key) % 256  # Basic operation for decryption

    decrypted_image = Image.fromarray(decrypted_data.astype(np.uint8))
    decrypted_image.save('decrypted_image.png')
    print("Image decrypted and saved as 'decrypted_image.png'")
    decrypted_image.show()  # Open the decrypted image

def main():
    while True:
        choice = input("Enter '1' to encrypt an image, '2' to decrypt an image, or 'q' to quit:\n")

        if choice == '1':
            image_path = input("Enter the path to the image to encrypt:\n")
            key = int(input("Enter the encryption key (an integer):\n"))
            encrypt_image(image_path, key)

        elif choice == '2':
            image_path = input("Enter the path to the image to decrypt:\n")
            key = int(input("Enter the decryption key (an integer):\n"))
            decrypt_image(image_path, key)

        elif choice == 'q':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()
