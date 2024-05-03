regex = r'(bba|b)*'

def gen_random_ab_string():
    import random
    return ''.join(random.choices('ab', k=random.randint(0, 10)))

def check_ab_string(s):
    # for each a: check if index -1, -2 is b
    for i, c in enumerate(s):
        if c == 'a':
            if i < 2:
                return False
            if s[i-1] != 'b' or s[i-2] != 'b':
                return False
    return True

def check_with_regex(regex):
    import re
    for _ in range(1000):
        s = gen_random_ab_string()
        if check_ab_string(s) != bool(re.fullmatch(regex, s)):
            print(s)

check_with_regex(regex)