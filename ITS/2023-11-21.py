import pwn


collection = []

def collect():
    # connect to c-ctr-0.itsec.cs.upb.de 10001
    r = pwn.remote('c-ctr-0.itsec.cs.upb.de', 10001)

    # send until get `> `
    r.recvuntil('> ')
    # send `1`
    r.sendline('1')
    # send username
    r.recvuntil('username\n> ')
    r.sendline('elikoga')
    # collect ciphertext:
    r.recvuntil('ciphertext:\n')
    ciphertext = r.recvline().strip()
    # parse as hex
    ciphertext = bytes.fromhex(ciphertext.decode())
    # print('ciphertext:', ciphertext)
    collection.append(ciphertext)

for i in range(2):
    collect()

differences = []
# first collection
c = collection[0]
# block size is 128bit = 16byte
first_block = c[:16]
for i in range(0, len(c) - 16, 16):
    # get block
    block = c[i:i+16]
    # print('block:', block)
    # get next block
    next_block = c[i+16:i+32]
    # print('next_block:', next_block)
    # get difference
    difference = pwn.xor(first_block, next_block)
    # print('difference:', difference)
    # save difference
    differences.append(difference)

# for each letter, choose first byte so that all others are printable
import string 
sol = []
for i in range(16):
    c = 0
    while True:
        # check if all others are printable
        ith_differences = [d[i] for d in differences]
        # check if all others are printable
        try:
            if all([chr(c ^ d) in string.printable for d in ith_differences]):
                # also check if it's valid for the other collections
                # save solution
                sol.append(c)
                break
        except:
            pass
        c += 1
        if c > 255:
            print('no solution found')
            break

decoded = []
for c in collection:
    key = pwn.xor(c[:16], sol   
                  )
    decoded.append(pwn.xor(key, c))

print(f"{decoded=}")
print(f"{sol=}")



