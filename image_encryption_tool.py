from PIL import Image
import numpy as np

def encrypt_image(image_path, key):
    # Open the image
    image = Image.open(image_path)
    # Convert image to numpy array
    image_array = np.array(image)
    
    # Encrypt the image using XOR operation with the key
    encrypted_array = image_array ^ key
    # Convert back to image
    encrypted_image = Image.fromarray(encrypted_array)
    
    return encrypted_image

def decrypt_image(encrypted_image, key):
    # Convert encrypted image to numpy array
    encrypted_array = np.array(encrypted_image)
    
    # Decrypt the image using XOR operation with the key
    decrypted_array = encrypted_array ^ key
    # Convert back to image
    decrypted_image = Image.fromarray(decrypted_array)
    
    return decrypted_image

def main():
    print("Image Encryption Tool")
    image_path = input("Enter the path of the image to encrypt: ")
    key = int(input("Enter a key (integer value between 0-255): "))
    
    # Ensure the key is within the valid range
    if key < 0 or key > 255:
        print("Key must be between 0 and 255.")
        return
    
    # Encrypt the image
    encrypted_image = encrypt_image(image_path, key)
    encrypted_image_path = "encrypted_image.png"
    encrypted_image.save(encrypted_image_path)
    print(f"Encrypted image saved as {encrypted_image_path}")
    
    # Decrypt the image
    decrypted_image = decrypt_image(encrypted_image, key)
    decrypted_image_path = "decrypted_image.png"
    decrypted_image.save(decrypted_image_path)
    print(f"Decrypted image saved as {decrypted_image_path}")

if __name__ == "__main__":
    main()