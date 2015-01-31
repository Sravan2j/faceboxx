import base64
from Crypto.Cipher import AES
from Crypto import Random
key = '12345'

def encrypt(raw):
    raw = pad(raw)
    iv = Random.new().read( AES.block_size )
    cipher = AES.new(key, AES.MODE_CBC, iv )
    return base64.b64encode( iv + cipher.encrypt( raw ) ) 

def decrypt(enc):
    enc = base64.b64decode(enc)
    iv = enc[:16]
    cipher = AES.new(key, AES.MODE_CBC, iv )
    return unpad(cipher.decrypt( enc[16:] ))

f= open('large_file.txt')
plain = f.read().replace('\n', '')
cipher = encrypt(plain)

fOut = open('encrypted','w')
fOut.write(cipher)

f= open('encrypted')
cipher = f.read().replace('\n', '')
decrypt(cipher)

