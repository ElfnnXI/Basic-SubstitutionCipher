import string
import random

class SubstitutionCipher:
    def __init__(self, key=None):
        self.alphabet = string.ascii_uppercase
        if key:
            self.key = key.upper()
        else:
            self.key = self.generate_key()
        self.encrypt_table = str.maketrans(self.alphabet, self.key)
        self.decrypt_table = str.maketrans(self.key, self.alphabet)

    def generate_key(self):
        shuffled = list(self.alphabet)
        random.shuffle(shuffled)
        return ''.join(shuffled)

    def encrypt(self, plaintext):
        plaintext = plaintext.upper()
        return plaintext.translate(self.encrypt_table)

    def decrypt(self, ciphertext):
        ciphertext = ciphertext.upper()
        return ciphertext.translate(self.decrypt_table)

if __name__ == "__main__":
    print("=== Basic Substitution Cipher ===")
    print("Choose an option:")
    print("1. Encrypt a message")
    print("2. Decrypt a message")
    choice = input("Enter your choice (1/2): ")

    if choice == '1':
        cipher = SubstitutionCipher()
        print(f"Generated Key (Save this key to decrypt later): {cipher.key}\n")
        confirm_key = input("Please re-enter the key to proceed: ").upper()

        if confirm_key != cipher.key:
            print("Error: The key does not match. Exiting.")
        else:
            message = input("Enter a message to encrypt: ")
            encrypted = cipher.encrypt(message)
            print(f"Encrypted message: {encrypted}")

    elif choice == '2':
        key = input("Enter the key to use for decryption: ").upper()
        cipher = SubstitutionCipher(key)
        message = input("Enter the message to decrypt: ")
        decrypted = cipher.decrypt(message)
        print(f"Decrypted message: {decrypted}")

    else:
        print("Invalid choice. Exiting.")
