def intersect(a: list, b: list) -> list:
    result = list()
    for i in a:
        if i in b:
            result.append(i)
    result.sort()
    return result


def subtract(a: list, b: list) -> list:
    result = list()
    for i in a:
        if i not in b:
            result.append(i)
    result.sort()
    return result


def union(a: list, b: list) -> list:
    result = b.copy()
    for i in a:
        if i not in b:
            result.append(i)
    result.sort()
    return result


a = [1, 2, 3, 4, 5]
b = [2, 5, 6, 3, 10, 18]
print("union", union(a, b))
print("intersect", intersect(a, b))
print("subtract", subtract(a, b))
print("subtract", subtract(b, a))
