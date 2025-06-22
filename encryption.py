import os
import logging
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import base64

def generate_key_from_password(password: str, salt: bytes) -> bytes:
    """Generate encryption key from password and salt"""
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
    )
    key = base64.urlsafe_b64encode(kdf.derive(password.encode()))
    return key

def encrypt_file(input_path: str, output_path: str, password: str) -> None:
    """Encrypt a file using Fernet encryption"""
    try:
        # Generate random salt
        salt = os.urandom(16)
        
        # Generate key from password
        key = generate_key_from_password(password, salt)
        fernet = Fernet(key)
        
        # Read and encrypt file
        with open(input_path, 'rb') as file:
            original_data = file.read()
        
        encrypted_data = fernet.encrypt(original_data)
        
        # Write salt + encrypted data
        with open(output_path, 'wb') as encrypted_file:
            encrypted_file.write(salt + encrypted_data)
            
        logging.info(f"File encrypted: {input_path} -> {output_path}")
        
    except Exception as e:
        logging.error(f"Error encrypting file: {e}")
        raise

def decrypt_file(input_path: str, output_path: str, password: str) -> None:
    """Decrypt a file using Fernet encryption"""
    try:
        # Read salt and encrypted data
        with open(input_path, 'rb') as encrypted_file:
            data = encrypted_file.read()
        
        # Extract salt and encrypted data
        salt = data[:16]
        encrypted_data = data[16:]
        
        # Generate key from password
        key = generate_key_from_password(password, salt)
        fernet = Fernet(key)
        
        # Decrypt data
        decrypted_data = fernet.decrypt(encrypted_data)
        
        # Write decrypted file
        with open(output_path, 'wb') as file:
            file.write(decrypted_data)
            
        logging.info(f"File decrypted: {input_path} -> {output_path}")
        
    except Exception as e:
        logging.error(f"Error decrypting file: {e}")
        raise