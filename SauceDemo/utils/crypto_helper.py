import os
from cryptography.fernet import Fernet

def get_cipher():
    key = os.getenv("SAUCE_SECRET_KEY")
    if not key:
        raise RuntimeError("SAUCE_SECRET_KEY not set")
    return Fernet(key.encode())


def encrypt(text: str) -> str:
    cipher = get_cipher()
    return cipher.encrypt(text.encode()).decode()


def decrypt(token: str) -> str:
    cipher = get_cipher()
    return cipher.decrypt(token.encode()).decode()
