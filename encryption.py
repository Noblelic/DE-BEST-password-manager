from cryptography.fernet import Fernet
import os

def key_main():
    if not os.path.exists('Encryption.key'):

        key = Fernet.generate_key()
        with open('Encryption.key','wb') as file:
          file.write(key)
          
    else:
        
        with open('Encryption.key', 'rb') as file:
          key = file.read()
    return key

def encrypt_password(password,key):
   cipher = Fernet(key)

   encrypted_password = cipher.encrypt(password.encode())
   return encrypted_password.decode()


def decrypt_password(encrypted_password,key):
   cipher = Fernet(key)

   decrypted_password = cipher.decrypt(encrypted_password.encode())
   return decrypted_password.decode()
   
    
