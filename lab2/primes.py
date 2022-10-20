import math


def is_prime(n):
    if n == 2:
        return True
    if n % 2 == 0 or n == 1 or n == 0:
        return False
    for i in range(3, math.floor(math.sqrt(n))):
        if n % i == 0:
            return False
    return True

numbers = [1, 2, 3, 5, 23, 24, 39, 14, 4]
result = list()
for x in numbers:
    if is_prime(x):
        result.append(x)
print(result)