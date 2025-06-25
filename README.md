# Substitution Cipher Python Implementation
A simple implementation of a cryptographic technique called **Substitution Cipher**, a classic encryption method, using Python. This script allows to encrypt and decrypt messages using randomly generated or customised substitution keys.

---

## 💪 Features

- Generates a random substitution key using all uppercase letters
- Encrypts plaintext using the substitution cipher method
- Decrypts ciphertext back to the original message

## 🙏 Requirements

* Python 3.x

## 🙈 How to Use

1. Clone this repository:

```bash
git clone https://github.com/ElfnnXI/Basic-SubstitutionCipher.git
cd Basic-SubstitutionCipher
```

2. Run the script:

```bash
python start.py
```

3. Follow the on-screen instructions to encrypt or decrypt messages.

## Example

```
Encryption:
=== Basic Substitution Cipher ===
Choose an option:
1. Encrypt a message
2. Decrypt a message
Enter your choice (1/2): 1
Generated Key (Save this key to decrypt later): NRYZGEMWQJHCBVKTIFUDALPXSO

Please re-enter the key to proceed: NRYZGEMWQJHCBVKTIFUDALPXSO
Enter a message to encrypt: Im falling in love u  R
Encrypted message: QB ENCCQVM QV CKLG A  F

Decryption:
=== Basic Substitution Cipher ===
Choose an option:
1. Encrypt a message
2. Decrypt a message
Enter your choice (1/2): 2
Enter the key to use for decryption: NRYZGEMWQJHCBVKTIFUDALPXSO
Enter the message to decrypt: QB ENCCQVM QV CKLG A  F
Decrypted message: IM FALLING IN LOVE U  R

```

## ⚙️ Custom Key (Optional)

You can modify the script to use a custom 26-character key instead of generating one randomly. Ensure your key contains all 26 unique uppercase letters.

---

## 🧑‍💻 Author
Ikmal Thaufan Mahdi
GitHub: @ElfnnXI

