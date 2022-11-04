#%%
import math
from math import exp, factorial
import numpy as np
from numpy import arange

#%%
def poly_exp(n):
    def poly(x):
        return sum([x**i / factorial(i) for i in range(n)])

    return poly


#%%
# we want the minimal n, such that poly_exp(n)(x) is accurate to acc

acc = 0.0001
range_low = 0
range_high = 0.1
step = 0.001


#%%
n = 1
while True:
    poly = poly_exp(n)
    for x in arange(range_low, range_high, step):
        if abs(poly(x) - exp(x)) > acc:
            break
    else:
        break
    n += 1

print(f"n = {n}")
