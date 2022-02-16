
from cryptography.fernet import Fernet

key = Fernet.generate_key()

#print (key)

file = open(b"kalienc.png","rb")

data = file.read()

file.close()

file_2 = open(b"kali.png","wb")

f = Fernet(b'9h_BLt5y_MD0GEzivPWL-Lm3UfufhN0-mTqfkk6CNkc=')

enc = f.decrypt(data)

file_2.write(enc)

file_2.close()

