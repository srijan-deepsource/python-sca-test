from cryptography.fernet import Fernet
import django

f = Fernet(b'')
django_path = django.__path__[0]
print(django_path)
print(f.encrypt(django_path.encode()))
