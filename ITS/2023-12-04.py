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




if __name__ == "__main__":
    res = padding_oracle_attack(get_ciphertext())
    print(f"Result: {res}")