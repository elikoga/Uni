# image.enc is a one time pad encrypted image, key is 10 bytes repeating.
# jpeg format
# so we expect FF D8 FF E0 00 10 4A 46 49 46 00 01

jpeg_magic = b'\xFF\xD8\xFF\xE0\x00\x10\x4A\x46\x49\x46\x00\x01'

with open('image.enc', 'rb') as f:
    data = f.read()

first_10_bytes = data[:10]
first_10_bytes_jpeg_magic = jpeg_magic[:10]

otp_key = bytes([a ^ b for a, b in zip(first_10_bytes, first_10_bytes_jpeg_magic)])

otp_key_original = otp_key

print(otp_key)

otp_key = otp_key * (len(data) // len(otp_key)) + otp_key[:len(data) % len(otp_key)]

decoded_image = bytes([a ^ b for a, b in zip(data, otp_key)])

with open('image.jpg', 'wb') as f:
    f.write(decoded_image)

# decode whoami too

with open('whoami', 'rb') as f:
    data = f.read()

otp_key = otp_key_original
otp_key = otp_key * (len(data) // len(otp_key)) + otp_key[:len(data) % len(otp_key)]

decoded_whoami = bytes([a ^ b for a, b in zip(data, otp_key)])

with open('whoami.jpg', 'wb') as f:
    f.write(decoded_whoami)

print(len(jpeg_magic))