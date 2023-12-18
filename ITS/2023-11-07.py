def h(m_im1, x_i):
    return m_im1 ^ x_i

m_0 = 2**8 - 1

def m_i(m, i):
    if i == 0:
        return m_0
    return h(m_i(m, i - 1), m[i - 1])

def mac(k, m):
    return (2**8 + (m_i(m, len(m)) + k)) % 2**8

def calc_key(mac, m):
    m_z = m_i(m, len(m))
    print_binary(m_z)
    print_binary(mac)
    return  (2**8 + (mac - m_z)) % 2**8

def print_binary(x):
    print("{:08b}".format(x))

def parse_binary(x):
    return int(x, 2)

if __name__ == "__main__":
    print_binary(calc_key(0b01010101, [ord(c) for c in "FILMABEND?"]))
    key = calc_key(0b01010101, [ord(c) for c in "FILMABEND?"])
    print_binary(key)
    unk_mac = 0b11001111
    candidates = [
        "MATRIX",
        "BATMAN",
        "TENET",
        "STARWARS",
        "DUNE",
        "LOTR"
    ]
    for candidate in candidates:
        print(candidate, mac(key, [ord(c) for c in candidate]), unk_mac)