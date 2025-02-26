import cryptography
import django

key = cryptography.hazmat.primitives.asymmetric.rsa.generate_private_key()
django_path = django.__path__[0]
print(django_path)
print(key)
