# def rank(c: str, p: int, S: str) -> int:
#     # rank of c in S[:p+1]
#     return S[:p+1].count(c)

import numpy as np
def rank(c: str, p: int, S: str) -> int:
    # rank of c in S[:p+1]
    c_uint8 = np.array(list(c), dtype=np.uint8)
    S_uint8 = np.array(list(S[:p+1]), dtype=np.uint8)
    return np.count_nonzero(S_uint8 == c_uint8[0])