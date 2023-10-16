from typing import Iterator, TypeVar
import random

class SortableChar:
    def __init__(self, char: str, original_index: int, is_eof_marker: bool = False):
        self.char = char
        self.original_index = original_index
        self.is_eof_marker = is_eof_marker
    
    def as_comparable(self):
        if self.is_eof_marker:
            return -1
        else:
            return ord(self.char.lower())
    
    def __lt__(self, other):
        return self.as_comparable() < other.as_comparable()
    
    def __eq__(self, other):
        return self.as_comparable() == other.as_comparable()
    
    def __repr__(self):
        if self.is_eof_marker:
            return f'EOF {self.char} ({self.original_index})'
        return f'{self.char} ({self.original_index})'

T = TypeVar('T')

def gen_rotations(s: list[T]) -> Iterator[list[T]]:
    for i in range(len(s)):
        yield s[i:] + s[:i]

def naive_bwt(s: list[SortableChar]) -> str:
    rotations = list(gen_rotations(s))
    sorted_rotations = sorted(rotations)
    if False: # debug
        for i, r in enumerate(sorted_rotations):
            print(i, r)
    return ''.join([x[-1].char for x in sorted_rotations])

def transform(s: str) -> str:
    # We'll treat the end of the string as a special character
    s1 = [SortableChar(c, i) if i != len(s) - 1 else SortableChar('$', i, True) for i, c in enumerate(s)]
    return naive_bwt(s1)

def prop_transform_is_permutation(s: str) -> bool:
    return set(transform(s)) == set(s)

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
            print(string)
            return False
    return True



if __name__ == '__main__':
    print(test_prop_bwt_str(prop_transform_is_permutation))
    abracadabra_bwt = transform('abracadabra$')
    print(f"{abracadabra_bwt=}, {abracadabra_bwt == 'ard$rcaaaabb'=}")