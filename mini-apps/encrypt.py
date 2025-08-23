import random
import string

def generate_key():
    chars = " " + string.punctuation + string.digits + string.ascii_letters
    chars = list(chars)
    key = chars.copy()
    random.shuffle(key)
    return chars, key

def show_menu():
    print("\nOptions:")
    print("1. Encrypt")
    print("2. Decrypt")
    print("3. Generate new key")
    print("4. Exit")
    return input("Enter your choice (1/2/3/4): ")

def main():
    print("Welcome to the Encryption/Decryption Program!")
    print("Generating a new encryption key...")
    chars, key = generate_key()
    
    while True:
        choice = show_menu()
        
        if choice == '1':
            # Encrypt
            plain_text = input("\nEnter a message to encrypt: ")
            cipher_text = ""
            for char in plain_text:
                if char in chars:
                    index = chars.index(char)
                    cipher_text += key[index]
                else:
                    cipher_text += char  # Keep characters not in the charset as is
            print(f"\nEncrypted message: {cipher_text}")
            
        elif choice == '2':
            # Decrypt
            cipher_text = input("\nEnter a message to decrypt: ")
            plain_text = ""
            for char in cipher_text:
                if char in key:
                    index = key.index(char)
                    plain_text += chars[index]
                else:
                    plain_text += char  # Keep characters not in the key as is
            print(f"\nDecrypted message: {plain_text}")
            
        elif choice == '3':
            # Generate new key
            print("\nGenerating a new encryption key...")
            chars, key = generate_key()
            print("New encryption key has been generated!")
            
        elif choice == '4':
            print("\nThank you for using the Encryption/Decryption Program!")
            break
            
        else:
            print("\nInvalid choice. Please enter 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()