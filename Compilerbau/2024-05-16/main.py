# takes a generator of chars, returns generator of tokens
from typing import Iterator


class Token:
    token_type: str
    # oneof integer, operator, lparen, rparen
    value: str

    def __init__(self, token_type, value):
        assert token_type in ["integer", "operator", "lparen", "rparen"]
        self.token_type = token_type
        self.value = value

    def __repr__(self):
        return f"Token({self.token_type}, '{self.value}')"


# automaton table: given state, input, new state
table = {
    0: {
        "0": 1,
        "1": 2,
        "2": 2,
        "3": 2,
        "4": 2,
        "5": 2,
        "6": 2,
        "7": 2,
        "8": 2,
        "9": 2,
        "+": 3,
        "-": 3,
        "*": 3,
        "/": 3,
        "^": 3,
        "(": 4,
        ")": 5,
    },
    1: {},
    # 2: {'0-9': 2},
    2: {"0": 2, "1": 2, "2": 2, "3": 2, "4": 2, "5": 2, "6": 2, "7": 2, "8": 2, "9": 2},
    3: {},
    4: {},
    5: {},
}

accepting = {1, 2, 3, 4, 5}


def lexer(chars):
    state = 0
    buffer = ""
    # call chars = next(chars) to get next char
    while True:
        try:
            c = next(chars)
        except StopIteration:
            break
        # if whitespace, ignore
        if c.isspace():
            continue
        if c == "\u02c6": # latex circumflex
            c = "^"
        if c in table[state]:
            # accepting transition, don't yield yet
            state = table[state][c]
            assert state in accepting
            buffer += c
        else:
            # not accepting transition, yield buffer
            # check state for type
            if state == 1 or state == 2:
                yield Token("integer", buffer)
            elif state == 3:
                yield Token("operator", buffer)
            elif state == 4:
                yield Token("lparen", buffer)
            elif state == 5:
                yield Token("rparen", buffer)
            # reset buffer
            buffer = ""
            # reset state to read c again
            try:
                state = table[0][c]
                buffer += c
            except KeyError:
                raise ValueError(f"Invalid character {c}")
    # yield last buffer
    assert state in accepting
    if buffer:
        # check state for type
        if state == 1 or state == 2:
            yield Token("integer", buffer)
        elif state == 3:
            yield Token("operator", buffer)
        elif state == 4:
            yield Token("lparen", buffer)
        elif state == 5:
            yield Token("rparen", buffer)


def test_lexer():
    print("# Testing lexer")
    good = [
        "2+3)*4^(2)",
        "1",
        "1-23^(456)",
        "3141592/(1*2)+42" "+4",
        "1+(2-3",
    ]
    bad = ["1.2", "I bims 1 String"]
    for s in good:
        print(f"Good: {s}")
        # print(list(lexer(iter(s))))
        print(f"Checking {s}")
        print(f"Lexer: {list(lexer(iter(s)))}")
        print("")
        # walk through using for loop
    for s in bad:
        try:
            print(f"Bad: {s}")
            # print(list(lexer(iter(s))))
            print(f"Checking {s}")
            print(f"Lexer: {list(lexer(iter(s)))}")
        except ValueError as e:
            # print(e)
            print(f"Lexer: {e}")
        print("")


test_lexer()

"""
E0 -> E1 E0'
E0' -> + E1 E0' | - E1 E0' | ε
E1 -> E2 E1'
E1' -> * E2 E1' | / E2 E1' | ε
E2 -> E3 E2'
E2' -> ^ ( E0 ) E2' | ε
E3 -> ( E0 ) | num | - E0
"""

"""
E0 -> E1 E0' # no node
E0' -> + E1 E0' # Plus
E0' -> - E1 E0' # Minus
E0' -> ε # no node
E1 -> E2 E1' # no node
E1' -> * E2 E1' # Mult
E1' -> / E2 E1' # Div
E1' -> ε # no node
E2 -> E3 E2' # no node
E2' -> ^ ( E0 ) E2' # Pow
E2' -> ε # no node
E3 -> ( E0 ) # Paren
E3 -> num # Num
E3 -> - E0 # Neg
"""

parse_node_types = [
    "Plus",
    "Minus",
    "Mult",
    "Div",
    "Pow",
    "Paren",
    "Num",
    "Neg",
]

class ParseNode:
    def __init__(self, node_type, children):
        assert node_type in parse_node_types
        self.node_type = node_type
        self.children = children
        self.value = None
        if node_type == "Num":
            assert len(children) == 1
            assert children[0].token_type == "integer"
            self.value = int(children[0].value)

    def __repr__(self):
        return f"ParseNode({self.node_type}, {self.children})"

def parse(tokens: Iterator[Token]):
    current = next(tokens)
    stack = []

    def accept(token_type, value=None, node_type=None):
        nonlocal current
        if current.token_type == token_type:
            last = current
            if value is not None and current.value != value:
                return False
            try:
                current = next(tokens)
            except StopIteration:
                current = type("Token", (), {"token_type": "end_of_string", "value": "end_of_string"})
            if node_type is not None:
                stack.append(ParseNode(node_type, [last]))
            return True
        return False

    def expect(token_type, value=None, node_type=None):
        nonlocal current
        if token_type == "end_of_string":
            if current.token_type == "end_of_string":
                return
            else:
                raise ValueError(f"Expected end of input, got {current.token_type}")
        if not accept(token_type, value, node_type):
            raise ValueError(f"Expected {token_type}, got {current.token_type}")


    def E0():
        E1()
        E0_()

    def E0_():
        if accept("operator", "+"):
            E1()
            right = stack.pop()
            left = stack.pop()
            stack.append(ParseNode("Plus", [left, right]))
            E0_()
        elif accept("operator", "-"):
            E1()
            right = stack.pop()
            left = stack.pop()
            stack.append(ParseNode("Minus", [left, right]))
            E0_()
        else:
            pass

    def E1():
        E2()
        E1_()

    def E1_():
        if accept("operator", "*"):
            E2()
            right = stack.pop()
            left = stack.pop()
            stack.append(ParseNode("Mult", [left, right]))
            E1_()
        elif accept("operator", "/"):
            E2()
            right = stack.pop()
            left = stack.pop()
            stack.append(ParseNode("Div", [left, right]))
            E1_()
        else:
            pass

    def E2():
        E3()
        E2_()

    def E2_():
        if accept("operator", "^"):
            expect("lparen")
            E0()
            expect("rparen")
            right = stack.pop()
            left = stack.pop()
            stack.append(ParseNode("Pow", [left, right]))
            E2_()
        else:
            pass

    def E3():
        if accept("lparen"):
            E0()
            expect("rparen")
            value = stack.pop()
            stack.append(ParseNode("Paren", [value]))
        elif accept("integer", None, "Num"):
            # parse num
            pass
        elif accept("operator", "-"):
            # expect("integer", None, "Num")
            E0()
            value = stack.pop()
            stack.append(ParseNode("Neg", [value]))
        else:
            raise ValueError(f"Expected integer or lparen, got {current.token_type}")

    E0()
    # print(f"Done reading input, current: {current.token_type}")
    expect("end_of_string")

    return stack.pop()

def test_parser():
    print("# Testing parser")
    good = [
        "(2+3)*4^(2)",
        "1",
        "1-23^(456)",
        "3141592/(1*2)+42",
        "1+(2-3)",
        "-2",
        "-2^(2)",
    ]
    bad = [") 1", "1 +", "1 + 2 )", "2^2"]
    for s in good:
        print(f"Good: {s}")
        print(f"Checking {s}")
        print(f"Parse: {parse(lexer(iter(s)))}")
        print("")
    for s in bad:
        try:
            print(f"Bad: {s}")
            print(f"Checking {s}")
            print(f"Parse: {parse(lexer(iter(s)))}")
        except ValueError as e:
            print(f"Parse: {e}")
        print("")

def interpret(node):
    if node.node_type == "Num":
        return node.value
    elif node.node_type == "Plus":
        return interpret(node.children[0]) + interpret(node.children[1])
    elif node.node_type == "Minus":
        return interpret(node.children[0]) - interpret(node.children[1])
    elif node.node_type == "Mult":
        return interpret(node.children[0]) * interpret(node.children[1])
    elif node.node_type == "Div":
        return interpret(node.children[0]) // interpret(node.children[1])
    elif node.node_type == "Pow":
        return interpret(node.children[0]) ** interpret(node.children[1])
    elif node.node_type == "Paren":
        return interpret(node.children[0])
    elif node.node_type == "Neg":
        return -interpret(node.children[0])
    else:
        raise ValueError(f"Unknown node type {node.node_type}")


def repl():
    while True:
        s = input("Enter expression: ")
        try:
            print(f"Lex: {list(lexer(iter(s)))}")
        except ValueError as e:
            import traceback
            traceback.print_exc()
        try:
            print(f"Parse: {parse(lexer(iter(s)))}")
        except ValueError as e:
            import traceback
            traceback.print_exc()
        try:
            print(f"Result: {interpret(parse(lexer(iter(s))))}")
        except ValueError as e:
            import traceback
            traceback.print_exc()

repl()