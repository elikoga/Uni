from pwn import *

# nc c-how-to-tcp-0.itsec.cs.upb.de 10000

s = remote('c-how-to-tcp-0.itsec.cs.upb.de', 10000)

# wait until "###END WELCOME###"
s.recvuntil('###END WELCOME###\n')
# next two lines are numbers
while True:
    a_str = s.recvline().strip()
    b_str = s.recvline().strip()
    print(a_str)
    print(b_str)
    # convert to integers
    a = int(a_str)
    b = int(b_str)
    # receive until "Bitte gib die Summe der obigen 2 Zahlen ein"
    s.recvuntil('Bitte gib die Summe der obigen 2 Zahlen ein\n')
    # send the sum
    s.sendline(str(a + b))
    # receive until "Richtig!"
    s.recvuntil('Richtig!\n')
