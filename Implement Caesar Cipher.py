def caesar_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():  # Check if the character is a letter
            shift_base = ord('A') if char.isupper() else ord('a')
            # Encrypt the character and wrap around the alphabet
            encrypted_char = chr((ord(char) - shift_base + shift) % 26 + shift_base)
            encrypted_text += encrypted_char
        else:
            encrypted_text += char  # Non-alphabetic characters are not changed
    return encrypted_text

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)  # Decrypting is just encrypting with the negative shift

def main():
    print("Caesar Cipher Program")
    while True:
        choice = input("Would you like to (E)ncrypt or (D)ecrypt? (Q to quit): ").strip().upper()
        if choice == 'Q':
            print("Exiting the program.")
            break
        elif choice in ['E', 'D']:
            message = input("Enter your message: ")
            shift = int(input("Enter the shift value (1-25): "))
            if choice == 'E':
                encrypted_message = caesar_encrypt(message, shift)
                print(f"Encrypted message: {encrypted_message}")
            elif choice == 'D':
                decrypted_message = caesar_decrypt(message, shift)
                print(f"Decrypted message: {decrypted_message}")
        else:
            print("Invalid choice. Please select E, D, or Q.")

if __name__ == "__main__":
    main()