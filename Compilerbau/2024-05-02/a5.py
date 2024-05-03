# takes a generator of chars, returns generator of tokens
class Token:
    token_type: str
    # oneof integer, operator, lparen, rparen
    value: str
    def __init__(self, token_type, value):
        assert token_type in ['integer', 'operator', 'lparen', 'rparen']
        self.token_type = token_type
        self.value = value

    def __repr__(self):
        return f'Token({self.token_type}, \'{self.value}\')'

# automaton table: given state, input, new state
table = {
    0: {'0': 1, '1': 2, '2': 2, '3': 2, '4': 2, '5': 2, '6': 2, '7': 2, '8': 2, '9': 2, '+': 3, '-': 3, '*': 3, '/': 3, '^': 3, '(': 4, ')': 5},
    1: {},
    # 2: {'0-9': 2},
    2: {'0': 2, '1': 2, '2': 2, '3': 2, '4': 2, '5': 2, '6': 2, '7': 2, '8': 2, '9': 2},
    3: {},
    4: {},
    5: {}
}

accepting = {1, 2, 3, 4, 5}

def lexer(chars):
    state = 0
    buffer = ''
    # call chars = next(chars) to get next char
    while True:
        try:
            c = next(chars)
        except StopIteration:
            break
        # if whitespace, ignore
        if c.isspace():
            continue
        if c in table[state]:
            # accepting transition, don't yield yet
            state = table[state][c]
            assert state in accepting
            buffer += c
        else:
            # not accepting transition, yield buffer
            # check state for type
            if state == 1 or state == 2:
                yield Token('integer', buffer)
            elif state == 3:
                yield Token('operator', buffer)
            elif state == 4:
                yield Token('lparen', buffer)
            elif state == 5:
                yield Token('rparen', buffer)
            # reset buffer
            buffer = ''
            # reset state to read c again
            try:
                state = table[0][c]
                buffer += c
            except KeyError:
                raise ValueError(f'Invalid character {c}')
    # yield last buffer
    if buffer:
        # check state for type
        if state == 1 or state == 2:
            yield Token('integer', buffer)
        elif state == 3:
            yield Token('operator', buffer)
        elif state == 4:
            yield Token('lparen', buffer)
        elif state == 5:
            yield Token('rparen', buffer)

# additionally, we want stricter checking for the lexer
# mainly: parentheses should be balanced
# and: operators should be surrounded by expressions
# and: the whole token stream should be a valid expression

def check_parentheses_and_expression(tokens):
    # stack = []
    non_negative_int = 0
    is_start_expr = True
    
    while True:
        try:
            token = next(tokens)
        except StopIteration:
            break
        if token.token_type == 'lparen':
            # stack.append(token)
            non_negative_int += 1
            is_start_expr = True
        elif token.token_type == 'rparen':
            # if not stack:
            if non_negative_int == 0:
                raise ValueError('Unbalanced parentheses')
            # stack.pop()
            non_negative_int -= 1
            is_start_expr = False
        elif token.token_type == 'operator':
            if is_start_expr:
                raise ValueError('Operator at start of expression')
            is_start_expr = True
        elif token.token_type == 'integer':
            is_start_expr = False
        else:
            raise ValueError('Invalid token')
        yield token
    # if stack:
    if non_negative_int != 0:
        raise ValueError('Unbalanced parentheses')
    if is_start_expr:
        raise ValueError('Operator at end of expression')
    
# let's check some expressions

"""
Prüft ob euer Lexer für den Beispielausdruck oben den korrekten Tokenstream erzeugt. Euer Stream /
eure Liste an Tokens sollte in etwa so aussehen (wobei Anführungszeichen “” hier Anfang und Ende einer
Zeichenkette markieren wie üblich für Zeichenketten (Strings) in vielen Programmiersprachen):
“(”, “2”, “+”, “3”, “)”, “*”, “4”, “ˆ”, “(”, “2”, “)”
Euer Lexer sollte u.a. auch folgende Zeichenketten akzeptieren:
1, 1 - 23ˆ(456), 3141592 / (1 * 2) + 42.
Euer Lexer sollte Zeichenketten, die keine arithmetischen Ausdrücke, der hier beschriebenen Sprache, sind,
ablehnen und einen Fehler melden, wie z.B. für die Zeichenketten:
1.2, + 4, 1 + (2 - 3, I bims 1 String
"""

def test_lexer():
    print('# Testing lexer')
    good = [
        '2+3)*4^(2)',
        '1',
        '1-23^(456)',
        '3141592/(1*2)+42'
        '+4',
        '1+(2-3',
    ]
    bad = [
        '1.2',
        'I bims 1 String'
    ]
    for s in good:
        print(f'Good: {s}')
        # print(list(lexer(iter(s))))
        print(f'Checking {s}')
        print(f'Lexer: {list(lexer(iter(s)))}')
        print("")
        # walk through using for loop
    for s in bad:
        try:
            print(f'Bad: {s}')
            # print(list(lexer(iter(s))))
            print(f'Checking {s}')
            print(f'Lexer: {list(lexer(iter(s)))}')
        except ValueError as e:
            # print(e)
            print(f'Lexer: {e}')
        print("")

test_lexer()

def testing_parser():
    print('Testing parser')
    good = [
        '1',
        '1-23^(456)',
        '3141592/(1*2)+42'
    ]
    bad = [
        '2+3)*4^(2)',
        '1.2',
        '+4',
        '1+(2-3',
        'I bims 1 String',
        '1+'
    ]
    for s in good:
        print(f'Good: {s}')
        print(f'Checking {s}')
        print(f'Parser: {list(check_parentheses_and_expression(lexer(iter(s))))}')
        print('')
    for s in bad:
        try:
            print(f'Bad: {s}')
            print(f'Checking {s}')
            print(f'Parser: {list(check_parentheses_and_expression(lexer(iter(s))))}')
        except ValueError as e:
            print(f'Parser: {e}')
        print('')


testing_parser()

def repl():
    while True:
        s = input('Enter expression: ')
        try:
            print(list(check_parentheses_and_expression(lexer(iter(s)))))
        except ValueError as e:
            # print lex and parse error
            try:
                print(f"Parse: {list(lexer(iter(s)))}")
            except ValueError as e:
                print(f"Lex error: {e}")
            print(f"Parse error: {e}")

repl()