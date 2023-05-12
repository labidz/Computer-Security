!pip install pycryptodome

!pip install crypto


from Crypto.Cipher import DES
from secrets import token_bytes

def get_key():
  key = token_bytes(8)
  print("key is (key)")
  return key


def encrypt(msg,key):
  cipher = DES.new(key,DES.MODE_EAX)
  nonce = cipher.nonce
  cipher_text,tag = cipher.encrypt_and_digest(msg.encode('ascii'))
  return cipher_text,tag,nonce
msg = "Hello"
key = get_key()
ct,tg,nc = encrypt(msg,key)
print(f"Plaintext: {msg} \nCipherText:{ct}")


def decrypt(ct,key,nonce,tag):
  cipher = DES.new (key,DES.MODE_EAX,nonce=nonce)
  plain_text = cipher.decrypt(ct)
  return plain_text


decrypt(ct,key,nc,tg)
