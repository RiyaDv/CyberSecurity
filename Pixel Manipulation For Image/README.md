# Image Encryption and Decryption Tool

This Python program allows users to encrypt and decrypt images using a simple pixel manipulation technique. It uses the Pillow library (PIL) for image processing.

## Features

- **Encryption**: Encrypts an image using a provided key.
- **Decryption**: Decrypts an encrypted image using the same key.
- **Display**: Automatically opens the encrypted or decrypted image after processing.

## How to Use

1. **Installation**:
   - Make sure Python 3 is installed on your system.
   - Install dependencies using `pip`:
     ```
     pip install -r requirements.txt
     ```

2. **Running the Program**:
   - Run the program by executing `python image_encrypt_decrypt.py`.
   - Follow the on-screen instructions:
     - Enter '1' to encrypt an image.
     - Enter '2' to decrypt an image.
     - Enter 'q' to quit the program.

3. **Encryption**:
   - Enter the path to the image you want to encrypt.
   - Enter an integer as the encryption key.
   - The encrypted image will be saved as `encrypted_image.png` and opened automatically.

4. **Decryption**:
   - Enter the path to the encrypted image (`encrypted_image.png`).
   - Enter the same encryption key used for encryption.
   - The decrypted image will be saved as `decrypted_image.png` and opened automatically.

5. **Exiting**:
   - Enter 'q' at any time to quit the program.

## Example

- Encrypt an image: `python image_encrypt_decrypt.py`
- Decrypt an image: `python image_encrypt_decrypt.py`

