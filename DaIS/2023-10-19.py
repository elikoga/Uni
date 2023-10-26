import numpy as np


def transform_naive(s: str):
    assert s[-1] == '$'
    rotations = [s[i:] + s[:i] for i in range(len(s))]
    return ''.join(s[-1] for s in sorted(rotations))

def rank_np(s: "np.array", c: "np.uint8", i: int):
    # assert is array of uint8
    assert s.dtype == np.uint8
    assert s.ndim == 1
    assert c.dtype == np.uint8
    return np.count_nonzero(s[:i + 1] == c)

eof_char = '$'
eof_uint8 = np.frombuffer(eof_char.encode(), dtype=np.uint8)[0]

def untransform(l: str):
    l_arr = np.frombuffer(l.encode(), dtype=np.uint8)
    eof_idx = np.where(l_arr == eof_uint8)[0][0]
    count = np.append(np.zeros(1, dtype=np.uint8), np.cumsum(np.bincount(l_arr)))
    idx = eof_idx
    out_arr = np.zeros(len(l), dtype=np.uint8)
    for i in range(len(l) - 1, -1, -1):
        c = l_arr[idx]
        out_arr[i] = c
        idx = count[c] + rank_np(l_arr, c, idx) - 1
    out = out_arr.tobytes().decode()
    return out

def allow_char(c: str):
    # allow only if not smaller than '$'
    return (c > eof_char) and (c <= '~')

from hypothesis import given, settings
from hypothesis.strategies import text



if __name__ == '__main__':
    # s = 'abracadabra$'
    # l = transform_naive(s)
    # print(l)
    # untransform(l)
    # print(untransform(l))


    with open('input.txt', 'r') as f:
        s = f.read()
    s = s.replace(' ', '%')
    s = s.replace('\n', '&')
    s = [c for c in s if allow_char(c)]
    s += [eof_char]
    s = ''.join(s)
    # with open('input-clean.txt', 'w') as f:
    #     f.write(s)
    l = transform_naive(s)
    # print(l)
    # with open('out.txt', 'w') as f:
    #     f.write(l)

    # with open('out.txt', 'r') as f:
    #     l = f.read()
    s = untransform(l)
    s = s.replace('%', ' ')
    s = s.replace('&', '\n')
    print(s)


    # @given(text(max_size=10000))
    # @settings(max_examples=5000)
    # def test_transform_invert(s):
    #     s = ''.join([c for c in s if allow_char(c)])
    #     s += eof_char
    #     print(s)
    #     assert untransform(transform_naive(s)) == s
    
    # test_transform_invert()