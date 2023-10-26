from typing import Generator


alphabet = "abcdefghijklmnopqrstuvwxyz "
eof_char = '$'

def get_sort_key(char: str) -> int:
    try:
        return alphabet.index(char)
    except ValueError:
        return -1

def gen_rotations(s: list) -> Generator[str, None, None]:
    for i in range(len(s)):
        yield s[i:] + s[:i]

def naive_bwt(s: "list[str]") -> str:
    rotations = list(gen_rotations(s))
    sorted_rotations = sorted(rotations, key=lambda x: [get_sort_key(y) for y in x])
    return ''.join([x[-1] for x in sorted_rotations])

def transform(S: str) -> str:
    return naive_bwt(S)

def count(S: str, C: str) -> int:
    # where C is a single character
    # Counts characters in S smaller than C
    count = 0
    for char in S:
        if get_sort_key(char) < get_sort_key(C):
            count += 1
    return count

def rank(c: str, p: int, S: str) -> int:
    # rank of c in S[:p+1]
    return S[:p+1].count(c)

def retransform(inp: str) -> str:
    # using rank and count
    eof_index = inp.index(eof_char)
    idx = eof_index
    output = ''
    for _ in inp:
        c = inp[idx]
        output = c + output
        idx = count(inp, c) + rank(c, idx, inp) - 1
    return output

import random

def prop_transform_is_permutation(s: str) -> bool:
    return set(transform(s)) == set(s)

def prop_retransform_is_inverse(s: str) -> bool:
    return retransform(transform(s)) == s

def test_prop_bwt_str(prop):
    # construct a bwt example string
    bag_of_words = ['banana', 'abracadabra', 'mississippi','simsalabim','racecar']
    for i in range(200):
        selected = []
        for j in range(3):
            selected.append(random.choice(bag_of_words))
        string = ' '.join(selected)
        string += '$'
        if not prop(string):
            print(f"failed on {string}, {prop.__name__}")
            return False
    return True



if __name__ == '__main__':
    print(test_prop_bwt_str(prop_transform_is_permutation))
    print(test_prop_bwt_str(prop_retransform_is_inverse))
    abracadabra_bwt = transform('abracadabra$')
    print(f"{abracadabra_bwt=}, {abracadabra_bwt == 'ard$rcaaaabb'=}")


    # Add at least one test case consisting of an original string and a retransformed string and check via asserts, if the transform an retransform method performs correctly for this input data.

    # Add a comment to explain, why this test case is a useful test case and describe, which typical mistake shall be covered by this test case.

    test_str = 'mississippi$'
    print(f"{test_str=} {transform(test_str)=} {retransform(transform(test_str))=}")