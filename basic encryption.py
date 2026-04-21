import os
from cryptography.fernet import Fernet

key_filename = 'mykey.key'
plaintext_filename = 'word.txt'
encrypted_filename = 'encrypted_word.txt'
decrypted_filename = 'decrypted_word.txt'

# --- Key Management ---
# Check if the key file exists
if not os.path.exists(key_filename):
    # If not, generate a new key and save it
    key = Fernet.generate_key()
    with open(key_filename, 'wb') as k_file:
        k_file.write(key)
    print(f"Generated new Fernet key and saved to '{key_filename}'")
else:
    # If it exists, load the key
    with open(key_filename, 'rb') as k_file:
        key = k_file.read()
    print(f"Loaded Fernet key from '{key_filename}'")

# Initialize Fernet cipher with the key
cipher = Fernet(key)

# --- Ensure plaintext_filename exists for encryption ---
if not os.path.exists(plaintext_filename):
    print(f"'{plaintext_filename}' not found. Creating a sample one.")
    with open(plaintext_filename, 'wb') as f:
        f.write(b"This is a secret message from word.txt!")
else:
    print(f"Using existing '{plaintext_filename}' for encryption.")

# --- Encryption ---
print(f"\n--- Encrypting '{plaintext_filename}' ---")
with open(plaintext_filename, 'rb') as p_file:
    plaintext_data = p_file.read()

encrypted_data = cipher.encrypt(plaintext_data)
with open(encrypted_filename, 'wb') as e_file:
    e_file.write(encrypted_data)
print(f"Encrypted '{plaintext_filename}' to '{encrypted_filename}'")

# --- Decryption ---
print(f"\n--- Decrypting '{encrypted_filename}' ---")
with open(encrypted_filename, 'rb') as e_file:
    data_to_decrypt = e_file.read()

decrypted_data = cipher.decrypt(data_to_decrypt)
with open(decrypted_filename, 'wb') as d_file:
    d_file.write(decrypted_data)
print(f"Decrypted '{encrypted_filename}' to '{decrypted_filename}'")

print("\nVerification:")
print(f"Original plaintext: {plaintext_data}")
print(f"Decrypted plaintext: {decrypted_data}")
if plaintext_data == decrypted_data:
    print("✅ Decryption successful and matches original plaintext!")
else:
    print("❌ Decryption failed to match original plaintext.")