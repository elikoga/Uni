import pwn
from tqdm import tqdm
from multiprocessing import Pool, Queue, Process

# nc c-poa-0.itsec.cs.upb.de 10002 

# r = pwn.remote('c-poa-0.itsec.cs.upb.de', 10002)
r = None

# r.recvuntil('> ')
# r.sendline('1')
# r.recvuntil('Input your username')
# r.recvuntil('> ')
# r.sendline('elikoga')
# ciphertext = r.recvline().decode('utf-8').strip()
# print(ciphertext)
# r.recvuntil('> ')

def get_ciphertext():
    global r
    if r is None:
        r = pwn.remote('c-poa-0.itsec.cs.upb.de', 10002)
    r.recvuntil('> ')
    r.sendline('1')
    r.recvuntil('Input your username')
    r.recvuntil('> ')
    r.sendline('elikoga')
    ciphertext = r.recvline().decode('utf-8').strip()
    print(ciphertext)
    r.recvuntil('> ')
    # r.close()
    # r = None
    return ciphertext
import time
import random
def check_ciphertext(ciphertext):
    print(f'Checking {ciphertext}')
    global r
    if r is None:
        # wait 1-5 seconds
        time.sleep(random.random() * 4 + 1)
        r = pwn.remote('c-poa-0.itsec.cs.upb.de', 10002)
    r.sendline('2')
    r.recvuntil('Enter message you want to check')
    r.recvuntil('> ')
    r.sendline(ciphertext)
    res = r.recvline().decode('utf-8').strip()
    print(res)
    r.recvuntil('> ')
    return "Valid" in res



def padding_oracle_attack(ciphertext):
    ciphertext = bytes.fromhex(ciphertext)
    # verify: ciphertext is valid
    print(f'Verifying {ciphertext.hex()}')
    assert check_ciphertext(ciphertext.hex())
    cipher_block_size = 16
    blocks = [ciphertext[i:i+cipher_block_size] for i in range(0, len(ciphertext), cipher_block_size)]
    clear_blocks = []
    for i in range(len(blocks) - 1, 0, -1):
        print(f'Block {i}')
        block_dec_bytes = b""
        for j in range(cipher_block_size - 1, -1, -1):
            print(f'Byte {j}')
            expected_padding = bytes([cipher_block_size - j]) * (cipher_block_size - j)
            for k in range(256):
                print(f'{expected_padding=}, {block_dec_bytes=}, {k=}')
                known_suffix = pwn.xor(expected_padding[1:], block_dec_bytes)
                print(f'Trying {k} with known suffix {known_suffix}')
                if check_ciphertext(((b"\x00" * j) + bytes([k]) + known_suffix + blocks[i]).hex()):
                    block_dec_bytes = bytes([k ^ expected_padding[-1]]) + block_dec_bytes
                    break
            else:
                raise Exception("No valid padding found")
            
            print(f'Block decrypted: {block_dec_bytes}')
        block_dec_bytes = pwn.xor(blocks[i - 1], block_dec_bytes)
        print(f'Block decrypted: {block_dec_bytes}')
        clear_blocks = [block_dec_bytes] + clear_blocks
    return b"".join(clear_blocks)

if __name__ == "__main__":
    res = padding_oracle_attack(get_ciphertext())
    print(f"Result: {res}")