"""
## 1. Generate an empty wavelet tree

Implement a function <code>makeEmptyWT</code> that can be called by

<code>WT = makeEmptyWT(binaryCodes)</code> 

and that generates an empty wavelet tree from a code table <code>binaryCodes</code> of binary codes. The parameter <code>binaryCodes</code> is a dictionary mapping characters to Strings (consisting of 1s and 0s) storing a binary code.

WT shall have the shape defined by the <code>binaryCodes</code>, i.e. each leaf node contains a different character occurring in the input string. For example, for the InputString  <code>'yabbaadabbaay'</code>, your binary code table could e.g. be <code>{'y':'101','a':'0','b':'11','d':'100'}</code>. This binary code table should then be represented by an empty wavelet tree with the following shape:

<code>
├--a
└--
   ├--
   |  ├--d
   |  └--y
   └--b  
</code>

<b>Hint:</b> Please use and extend the given class Node that represents a binary tree with any kind of String data stored in each node.
Please make sure that the function <code>toString(self)</code> is not corrupted, because otherwise the asserts in the automatic tests will fail.
You can use the function <code>pprint(self)</code> to get a "human-readable" printout of your binary tree.
"""

class Node:

    # Simple binary tree with left and right child and (String) data
    def __init__(self, data):

        self.left = None
        self.right = None
        self.data = data

    # returns a string representation of the form "data(left,right)"
    def toString(self):
        l,r = "",""
        if self.left != None:
            l = self.left.toString()
        if self.right != None:
            r = self.right.toString()

        return self.data + "("+ l + "," + r + ")"
    
    # pretty prints the binary tree
    def pprint(self):
        self.pprint_rec("", "n")
   
    # recursive inner function of the pprint function
    def pprint_rec(self,indent, position):
        branch = ""
        if (position=="l"):
            branch="├--"
        elif (position=="r"):
            branch= "└--"
        print(indent + branch + self.data)
        prefix = "   "
        if(position=="l"):
            prefix = "|  "
        elif(position=="n"):
            prefix=""

        if self.left != None:
            self.left.pprint_rec(indent+prefix, "l")
        if self.right != None:
            self.right.pprint_rec(indent+prefix, "r")        

# End of class Node

#test:
#yabbaadabbaay
output = "(a(,),((d(,),y(,)),b(,)))"
binaryCodes = {'y':'101','a':'0','b':'11','d':'100'}
result = makeEmptyWT(binaryCodes).toString()
assert result==output, "Test failed for input {} and output {}. (Expected output: {})".format(binaryCodes, result, output)

#ttobbeornottttobbeorttobbeeornott
output = "((b(,),o(,)),((e(,),(n(,),r(,))),t(,)))"
binaryCodes = {'t': '11', 'o': '01', 'b': '00', 'e': '100', 'r': '1011', 'n': '1010'}
result = makeEmptyWT(binaryCodes).toString()
assert result==output, "Test failed for input {} and output {}. (Expected output: {})".format(binaryCodes, result, output)

def makeEmptyWT(binaryCodes: dict) -> Node:
    root = Node("")
    # binaryCodes: dictionary with characters as keys and binary codes as values
    # strategy: since we need to inspect the entire input anyways, we can iterate through all characters, look
    # at their tree traversal path and fill in the nodes along the way
    # i don't believe this could be done any faster than O(n) anyways, since we need to inspect all characters

    for char, code in binaryCodes.items():
        node = root
        for idx, bit in enumerate(code):
            if bit == "0":
                if node.left is None:
                    node.left = Node("")
                node = node.left
            elif bit == "1":
                if node.right is None:
                    node.right = Node("")
                node = node.right
            else:
                raise ValueError("Bad character {} at index {} in code {} for character {}".format(bit, idx, code, char))
        node.data = char
    
    return root

"""

## 2. Utility method ins

Implement a function <code>ins</code> that can be called by

<code>ins( bitString, bit, pos )</code>

and that inserts a <code>bit</code> (0 or 1) at the index <code>pos</code> (start counting pos from 0) into the bit string <code>bitString</code>. Bits at higher positions shall be shifted one position to the right.

"""

def ins(bitstring: str, bit: str, pos: int) -> str:
    # bitstring: string of bits (0s and 1s)
    # bit: string of one bit (0 or 1)
    # pos: index where to insert the bit (start counting pos from 0)
    return bitstring[:pos] + bit + bitstring[pos:]


"""
## 3. Insert a binary code into a wavelet tree

Implement a function <code>insertWT</code> that can be called by

<code>insertWT( waveletTree, binaryCode, pos )</code>

and that inserts the binary code of a character at the position <code>pos</code> (start counting pos at 0) into the wavelet tree. 

For example, if we want to insert the binary code <code>‘100’</code> (of the character ‘d’) at position 0 into the wavelet tree, we have to do the following.

1. Insert a <code>‘1’</code> bit at position <code>0</code> (i.e. before all other bits) into the bit sequence of the wavelet tree’s root node.
2. Insert a <code>‘0’</code> bit at position <code>0</code> (i.e. before all other bits) into the bit sequence of the wavelet tree’s root node’s right child.
3. Insert a <code>‘0’</code> bit at position <code>0</code> (i.e. before all other bits) into the bit sequence of the wavelet tree’s root node’s right child’s left child.

<b>Hint</b>: Of course, we do not only insert at position 0 or append the code to the end of each node. If we want to insert at an inner position, we have to compute the new position where to insert in the child node afterwards. In order to compute the correct insert position of a bit of a binary code into the bit sequence existing already at an inner wavelet tree node, we can apply the <code>rank</code> function to the parent wavelet tree node. Here, the rank function of Assignment 1 can be reused.

"""

def rank(c: str, p: int, S: str) -> int:
    # rank of c in S[:p+1]
    return S[:p+1].count(c)

def insertWT(waveletTree: Node, binaryCode: str, pos: int):
    current_node = waveletTree
    # print(f"Inserting code {binaryCode} at position {pos} into tree {waveletTree.toString()}")
    for idx, bit in enumerate(binaryCode):
        # print(f"Inserting bit {bit} at position {pos} into node {current_node.data}")
        if bit == "0":
            current_node.data = ins(current_node.data, bit, pos)
            pos = rank(bit, pos-1, current_node.data)
            current_node = current_node.left
        elif bit == "1":
            current_node.data = ins(current_node.data, bit, pos)
            pos = rank(bit, pos-1, current_node.data)
            current_node = current_node.right
        else:
            raise ValueError("Bad character {} at index {} in code {}".format(bit, idx, binaryCode))

"""
## 4. Read characters from a wavelet tree

Implement a function <code>readWT</code> that can be called by

<code>ch = readWT( waveletTree, pos )</code>

and that reads a character stored at the position <code>pos</code> (start counting at 0) from the wavelet tree. Continuing the previous example, if we read the character at position 0, we want to get ch=’y’.
"""

def readWT(waveletTree: Node, pos: int) -> str:
    current_node = waveletTree
    while (current_node.left is not None) or (current_node.right is not None):
        bit = current_node.data[pos]
        pos = rank(bit, pos-1, current_node.data)
        if bit == "0":
            current_node = current_node.left
        elif bit == "1":
            current_node = current_node.right
        else:
            raise ValueError("Bad character {} at index {} in node {}".format(bit, pos, current_node.data))
    return current_node.data

"""
## 6. Adding futher test cases

Choose one of the tasks 3 and 4 and add at least one test case that tests the method implemented in this task (either insert at a given position into a given Wavelet tree or read a letter at a given position from a given Wavelet tree).

Add a comment to explain, why this test case is a useful test case and describe, which typical mistake shall be covered by this test case.
"""

import random

tables = [
    {'y':'101','a':'0','b':'11','d':'100'},
    {'t': '11', 'o': '01', 'b': '00', 'e': '100', 'r': '1011', 'n': '1010'},
    {'a':'0000','b':'000100', 'c':'000101', 'd':'00011','e':'001','f':'010000',
    'g':'010001','h':'01001','i':'0101','j':'01100000','k':'01100001','l':'0110001',
    'm':'011001','n':'01101','o':'0111','p':'10000','q':'10001','r':'1001','s':'101',
    't':'110','u':'1110','v':'111100','w':'111101','x':'111110','y':'1111110','z':'1111111'}
]

def len_wavelet_tree(wavelet_tree: Node) -> int:
    return len(wavelet_tree.data)

def assert_str_and_wt_are_equal(string: str, wavelet_tree: Node):
    for pos in range(len_wavelet_tree(wavelet_tree)):
        assert string[pos] == readWT(wavelet_tree, pos), "String and wavelet tree are not equal at position {}".format(pos)

def prop_wavelet_tree_behaves_like_a_string(table: dict):
    wavelet_tree = makeEmptyWT(table)
    string = ""
    # so: in a series of random writes and reads, the wavelet tree should behave like a string
    for _ in range(1000):
        assert_str_and_wt_are_equal(string, wavelet_tree)
        # read or write?
        if len_wavelet_tree(wavelet_tree) == 0 or random.random() < 0.5:
            # write a random character at a random position
            char = random.choice(list(table.keys()))
            pos = random.randint(0, len_wavelet_tree(wavelet_tree))
            insertWT(wavelet_tree, table[char], pos)
            string = ins(string, char, pos)
        else:
            # read a random character at a random position
            pos = random.randint(0, len_wavelet_tree(wavelet_tree)-1)
            char = readWT(wavelet_tree, pos)
            assert string[pos] == char, "String and wavelet tree are not equal at position {}".format(pos)
        assert_str_and_wt_are_equal(string, wavelet_tree) # for good luck

for table in tables:
    prop_wavelet_tree_behaves_like_a_string(table)