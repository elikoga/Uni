debug = True

def transform(s: str) -> (str, int):
    rotations = [s[i:] + s[:i] for i in range(len(s))]
    rotations_with_index = [(rot, i) for i, rot in enumerate(rotations)]
    if debug:
        print("Rotations:")
        for rot in rotations_with_index:
            print(f"{rot[1]}: {rot[0]}")
    rotations_with_index.sort()
    if debug:
        print("Sorted rotations:")
        for rot in rotations_with_index:
            print(f"{rot[1]}: {rot[0]}")
    eof_index = [rot[1] for rot in rotations_with_index].index(0)
    return ("".join([rot[0][-1] for rot in rotations_with_index]), eof_index)

import numpy as np

def rank_np(s: "np.array", c: "np.uint8", i: int):
    # assert is array of uint8
    assert s.dtype == np.uint8
    assert s.ndim == 1
    assert c.dtype == np.uint8
    return np.count_nonzero(s[:i + 1] == c)


def untransform(l: str, eof_index: int):
    l_arr = np.frombuffer(l.encode(), dtype=np.uint8)
    count = np.append(np.zeros(1, dtype=np.uint8), np.cumsum(np.bincount(l_arr)))
    idx = eof_index
    out_arr = np.zeros(len(l), dtype=np.uint8)
    for i in range(len(l) - 1, -1, -1):
        c = l_arr[idx]
        out_arr[i] = c
        idx = count[c] + rank_np(l_arr, c, idx) - 1
        if (i != (len(l) - 1)) and (i != 0) and idx == eof_index:
            raise ValueError(f"Precondition violated: l: '{l}' is not a valid BWT string: LF is not a complete cycle")
    out = out_arr.tobytes().decode()
    return out

def untransform_with_dollar(l: str):
    eof_index = l.index("$")
    return untransform(l, eof_index)[:-1]

def prop_retransform_is_inverse(s: str) -> bool:
    return untransform(*transform(s)) == s
import random
def test_prop_bwt_str(prop):
    # construct a bwt example string
    bag_of_words = ['banana', 'abracadabra', 'mississippi','simsalabim','racecar']
    for i in range(2000):
        selected = []
        for j in range(3):
            selected.append(random.choice(bag_of_words))
        string = ' '.join(selected)
        # string += '$'
        if not prop(string):
            print(f"failed on {string}, {prop.__name__}")
            return False
    # also test on completely random strings
    length = random.randint(1, 10)
    alphabet = "abcdefghijklmnopqrstuvwxyz "
    for i in range(2000):
        string = "".join([random.choice(alphabet) for _ in range(length)])
        if not prop(string):
            print(f"failed on {string}, {prop.__name__}")
            return False
    return True

# test_prop_bwt_str(prop_retransform_is_inverse)

S1 = "banana"
print(f"S1: {S1}, BWT(S1): {transform(S1)}")
S2 = "anaban"
print(f"S2: {S2}, BWT(S2): {transform(S2)}")

S4 = "s$nnaaa"
S3 = untransform_with_dollar(S4)
print(f"S4: {S4}, S3=UnBWT(S4): {S3}")

S6 = "baaad"
S6_idx = 2
S5 = untransform(S6, S6_idx)
print(f"S6: {S6}, S5=UnBWT(S6): {S5}")