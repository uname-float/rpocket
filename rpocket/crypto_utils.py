import base64

from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

# Funzione per generare una chiave crittografica
def generate_key(password):
    salt = b'salt_'  # Salt casuale
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    key = kdf.derive(password.encode())

    # Codifica la chiave in base64 e assicurati che sia url-safe
    base64_key = base64.urlsafe_b64encode(key)

    # Se la chiave è più lunga di 32 byte, troncala
    #if len(base64_key) > 32:
    #    base64_key = base64_key[:32]
    # Se la chiave è più corta di 32 byte, aggiungi padding
    #elif len(base64_key) < 32:
    #    base64_key += b'=' * (32 - len(base64_key))

    return base64_key

# Funzione per criptare il CIV utilizzando la chiave crittografica
def encrypt_cvv(cvv, key):
    f = Fernet(key)
    encrypted_cvv = f.encrypt(cvv.encode())
    return encrypted_cvv


# Funzione per decriptare il CIV utilizzando la chiave crittografica
def decrypt_cvv(encrypted_cvv, key):
    f = Fernea(key)
    decrypted_cvv = f.decrypt(encrypted_cvv)
    return decrypted_cvv.decode()

