

def eli_pow(x, n):
  result = 1
  while n > 0:
    if n % 2 == 1:
      result = result * x
    x = x * x
    n = (n - (n % 2)) / 2 # rechtsshift
  return result

# I(n) := result * (x_var^n_var) = x_0 ^ n^0

# x_i, n_i, result_i
# x_{i+1} = x_i \cdot x_i
# n_{i+1} = \lfloor n_i / 2 \rfloor
# result_{i+1} = result_i \cdot x^{n_i \mod 2}

# result_i \cdot x^{n_i \mod 2} \cdot x_i \cdot x_i \cdot \lfloor n_i / 2 \rfloor

def david_pow(x, n):
  result = 1
  while n > 1:
    if n % 2 == 1:
      result = result * x
    x = x * x
    n = n // 2
  return result * x

# print values for pow(3, n) for n to 10

for n in range(0, 11):
  print("Real:" + str(pow(3, n)))
  print("Eli:" + str(eli_pow(3, n)))
  print("David:" + str(david_pow(3, n)))