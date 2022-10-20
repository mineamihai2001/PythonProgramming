def fibonacci(n):
    a = 0
    b = 1
    result = [a, b]
    for i in range(n - 2):
        c = a+b
        result.append(c)
        a = b
        b = c
    return result

print(fibonacci(10))