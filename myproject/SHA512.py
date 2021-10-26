import hashlib, binascii

#dk = hashlib.pbkdf2_hmac('sha512', b'password', b'some', 10000)
#print(binascii.hexlify(dk))
id="7+1"
m = hashlib.sha512()
m.update(id.encode('utf-8'))
print(m.hexdigest())
