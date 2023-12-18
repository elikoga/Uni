def computeFrequencies(inputString: str) -> dict:
    # return a dictionary of frequencies of characters in inputString
    freq = {}
    for c in inputString:
        if c in freq:
            freq[c] += 1
        else:
            freq[c] = 1
    return freq


# This test will only work if you have implemented task 1 correctly!

# toCompress = "yabbaadabbaay"

# freq = computeFrequencies(toCompress)
# huff = huffmanCode(freq)

# assert huff['y']=='101'
# assert huff['a']=='0'
# assert huff['b']=='11'
# assert huff['d']=='100'

# toCompress = "ttobbeornottttobbeorttobbeeornott"

# freq = computeFrequencies(toCompress)
# huff = huffmanCode(freq)

# assert huff['t']=='11'
# assert huff['o']=='01'
# assert huff['b']=='00'
# assert huff['e']=='100'
# assert huff['r']=='1011'
# assert huff['n']=='1010'


"""
<b>Hint</b>: You can compute the Huffman code with the help of two dictionaries:
* frequencies: <code>{key:list_of_characters/string; value:sum_of_frequencies}</code>
* huffman_codes: <code>{key: character; value: bits}</code>
"""

import heapq
import itertools





def huffmanCode_naive(frequencyTable: dict) -> dict:
    frequencies = {}
    huffman_codes = {}
    for key in frequencyTable:
        frequencies[key] = frequencyTable[key]
    while len(frequencies) > 1:
        # find the two smallest frequencies
        smallest = heapq.nsmallest(2, frequencies, key=frequencies.get)
        # create a new node with the two smallest frequencies as children
        new_node = (smallest[0], smallest[1])
        # add the new node to the frequency table
        frequencies[new_node] = frequencies[smallest[0]] + frequencies[smallest[1]]
        # remove the two smallest frequencies from the frequency table
        del frequencies[smallest[0]]
        del frequencies[smallest[1]]
    # create the huffman codes
    # by traversing the tree
    tree = next(iter(frequencies))
    # print(tree)
    stack = [(tree, "")]
    while stack:
        node, code = stack.pop()
        if isinstance(node, tuple):
            stack.append((node[0], code + "0"))
            stack.append((node[1], code + "1"))
        else:
            huffman_codes[node] = code
    # print(huffman_codes)
    return huffman_codes


import timeit

# if __name__ == "__main__":
#     print(timeit.timeit(lambda: huffmanCode({"a": 4, "b": 2, "c": 1, "d": 1})))
#     print(timeit.timeit(lambda: huffmanCode_naive({"a": 4, "b": 2, "c": 1, "d": 1})))

def encode(inputString, codeTable):
    return "".join(codeTable[c] for c in inputString)


def decode(huffmanCode, codeTable):
    tree = [[], []]
    # populate the tree
    for char, code in codeTable.items():
        node = tree
        for bit in code:
            if bit == "0":
                if not node[0]:
                    node[0] = [[], []]
                node = node[0]
            else:
                if not node[1]:
                    node[1] = [[], []]
                node = node[1]
        node[0] = char
        del node[1]
    
    decoded = ""
    node = tree
    # print(tree)
    for bit in huffmanCode:
        if bit == "0":
            node = node[0]
        else:
            node = node[1]
        if len(node) == 1:
        # if isinstance(node, str):
            decoded += node[0]
            node = tree
    return decoded

def real_encode(inputString):
    table = huffmanCode(computeFrequencies(inputString))
    return encode(inputString, table), table

import random
import string
def test_on_random_string(length):
    s = "".join(random.choice(string.ascii_letters) for _ in range(length))
    assert decode(*real_encode(s)) == s, (s, real_encode(s))

def test_on_random_strings():
    for _ in range(1000000):
        test_on_random_string(random.randint(0, 10))

if __name__ == "__main__":
    print(real_encode("yabbaadabbaay"))
    print(decode(*real_encode("yabbaadabbaay")))
    test_on_random_strings()
    # print(timeit.timeit(lambda: decode(*real_encode("yabbaadabbaay"))))