def set_operations(a: list, b: list) -> list:
    intersection = set(a).intersection(b)
    union = set().union(a, b)
    a_minus = set(a).difference(b)
    b_minus = set(b).difference(a)
    return [intersection, union, a_minus, b_minus]

result = set_operations([1, 2, 3 ,4], [2, 3, 5])
print("intersection: ", result[0])
print("union: ", result[1])
print("a/b: ", result[2])
print("b/a: ", result[3])
print(result)