from cryptography.fernet import Fernet


key = Fernet.generate_key()
token = f.encrypt(b"A really secret message. Not for prying eyes.")
