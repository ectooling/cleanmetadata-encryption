import os
from encryption import encrypt_file, decrypt_file

# Test parameters
password = "testpassword123"
original_file = "sample_input.txt"
encrypted_file = "sample_encrypted.bin"
decrypted_file = "sample_decrypted.txt"

# Create a sample file to encrypt
with open(original_file, "w") as f:
    f.write("This is a test message for encryption.")

# Encrypt the file
print(f"Encrypting {original_file} -> {encrypted_file}")
encrypt_file(original_file, encrypted_file, password)

# Decrypt the file
print(f"Decrypting {encrypted_file} -> {decrypted_file}")
decrypt_file(encrypted_file, decrypted_file, password)

# Verify content match
with open(original_file, "r") as f1, open(decrypted_file, "r") as f2:
    original_content = f1.read()
    decrypted_content = f2.read()

if original_content == decrypted_content:
    print("✅ Success: Decrypted content matches original.")
else:
    print("❌ Error: Decrypted content does not match original.")

# Clean up (optional)
os.remove(original_file)
os.remove(encrypted_file)
os.remove(decrypted_file)
