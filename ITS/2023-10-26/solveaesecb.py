# whoami is AES 128 ECB (no salt) encrypted

key = b'doggo fren'

with open('whoami', 'rb') as f:
    data = f.read()

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad


# key = pad(key, 128 // 8)
# fill up key by repeating it
key_len = 128 // 8
key = (key * (key_len // len(key) + 1))[0:key_len]


cipher = AES.new(key, AES.MODE_ECB)

data_pad = pad(data, 128 // 8)

plaintext = cipher.decrypt(data_pad)

# write decrypted data to file
with open('whoami.dec', 'wb') as f:
    f.write(plaintext)
doggo frendoggo 