
def gen_rotations(inp: list):
    for i in range(len(inp)):
        yield inp[i:] + inp[:i]

def char_comparable(char):
    # makes $ -1, all other chars map to int
    if char == '$':
        return -1
    else:
        return ord(char)

def magic_transform(inp: str):
    inp = list(inp)
    rotations = list(gen_rotations(inp))
    rotations_enumerated = list(enumerate(rotations))
    # sorted_rotations = sorted(rotations, key=lambda x: [char_comparable(y) for y in x])
    sorted_rotations = sorted(rotations_enumerated, key=lambda x: [char_comparable(y) for y in x[1]])
    start_index = sorted_rotations.index((0, inp))
    last_column = ''.join([x[1][-1] for x in sorted_rotations])
    return last_column, start_index

# def untransform(inp: str):
#     # sort and store indices

#     firsts = sorted(enumerate(inp), key=lambda x: char_comparable(x[1]))
#     l_to_f_indices = [x[0] for x in firsts]
#     f_to_l_indices = [x[0] for x in sorted(enumerate(l_to_f_indices), key=lambda x: x[1])]
#     curr_index = 0
#     decoded = [inp[curr_index]]
#     for i in range(len(inp)-1):
#         curr_index = f_to_l_indices[curr_index]
#         decoded.append(inp[curr_index])
#     return ''.join(decoded[:-1][::-1])

def untransform_new(inp: (str, int)):
    counts = {}
    for idx, char in enumerate(inp[0]):
        if char not in counts:
            counts[char] = 0
        counts[char] += 1
    start_index = inp[1]
    keys = sorted(counts.keys(), key=lambda x: char_comparable(x))
    counts_smaller = [0]
    for idx, key in enumerate(keys):
        if idx == 0:
            continue
        counts_smaller.append(counts_smaller[-1] + counts[keys[idx-1]])
    
    def rank(c, l, p):
        # rank of c in l[:p]
        return l[:p].count(c)

    # p = start_index
    # i = len(inp)
    # decoded = []
    # while i > 0:
    #     i -= 1
    #     c = inp[p]
    #     p = counts_smaller[keys.index(c)] + rank(c, inp, p)
    #     decoded.append(c)
    p = start_index
    output = ''
    for i in range(len(inp[0])):
        c = inp[0][p]
        p = counts_smaller[keys.index(c)] + rank(c, inp[0], p)
        output = c + output
    return output
        

untransform = untransform_new
    
def main():
    # inp = input()
    alphabet = 'abcd '
    # prop: for all strings of alphabet: untransform . magic_transform = id
    def prop(inp: str):
        return untransform(magic_transform(inp)) == inp
    import itertools
    import random
    for i in range(1000):
        # inp = ''.join(random.choices(alphabet, k=10))
        inp = ''
        for j in range(10):
            inp += random.choice(alphabet)
        inp += '$'
        if not prop(inp):
            print(inp)
            break
    else:
        print('passed')
    # inp = 'abracadabra'
    print(f"{inp=}")
    print(f"{magic_transform(inp)=}")
    print(f"{untransform(magic_transform(inp))=}")
    pass

if __name__ == '__main__':
    main()