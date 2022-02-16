
from cryptography.fernet import Fernet


key = Fernet.generate_key()

print (key,"\n")

s = b"hello world"

enc_text = b'gAAAAABdDc4JPA5HnaY7Fmo8pQYHzd7NV2yAMKaX8xUqzGJ_i3FgI8h_pQmmobD3hkmsRedvJra_akscDrGX5RuKqQT1xSNoRw=='

f = Fernet(b'B6Mc021O3qenW-grYkX2PKyRIGu_qQ23sN8ssnpTWYE=')

enc = f.decrypt(enc_text)

print (enc)












