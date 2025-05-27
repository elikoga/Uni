def h(m_im1, x_i):
    return m_im1 ^ x_i

# m_0 = 2**8 - 1
# m_0 = ""
def parse_binary(x):
    return int(x, 2)
# m_0 = parse_binary("10000011")
m_0 = 0b10000011

def m_i(m, i):
    if i == 0:
        return m_0
    return h(m_i(m, i - 1), m[i - 1])

def mac(k, m):
    return (m_i(m, len(m)) + k) % 256

def calc_key(mac, m):
    m_z = m_i(m, len(m))
    # print_binary(m_z)
    # print_binary(mac)
    return (mac - m_z) % 256

# def print_binary(x):
#     print("{:08b}".format(x))


if __name__ == "__main__":
    # print_binary(calc_key(0b00111101, [ord(c) for c in "FILMABEND?"]))
    key = calc_key(0b00111101, [ord(c) for c in "SPIELEABEND?"])
    # print_binary(key)
    print(f"Key: {key:08b}")
    # unk_mac = 0b11001111
    # candidates = [
    #     "MATRIX",
    #     "BATMAN",
    #     "TENET",
    #     "STARWARS",
    #     "DUNE",
    #     "LOTR"
    # ]
    unk_mac = 0b00011100
    candidates = [
        "UNO",
        "DSA",
        "CATAN",
        "MONOPOLY",
        "DND",
        "SCHACH"
    ]
    print(f"Unknown MAC: {unk_mac:08b}")
    for candidate in candidates:
        candidate_mac = mac(key, [ord(c) for c in candidate])
        print(f"{candidate}: {candidate_mac:08b} (key: {key:08b})")
        if candidate_mac == unk_mac:
            print(f"Found matching candidate: {candidate}")
    # for candidate in candidates:
    #     print(candidate, mac(key, [ord(c) for c in candidate]), unk_mac)