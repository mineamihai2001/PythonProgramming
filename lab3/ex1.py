def set_operations(a: set, b: set) -> list:
    intersection = set()
    union = set()
    a_minus = set()
    b_minus = set()
    for i in a:
        union.add(i)
        if i in b:
            intersection.add(i)
        else: 
            a_minus.add(i)
    for j in b:
        if j not in a:
            b_minus.add(j)
    return [intersection, union, a_minus, b_minus]

result = set_operations({1, 2, 3 ,4}, {2, 3, 5})
print("intersection: ", result[0])
print("union: ", result[1])
print("a/b: ", result[2])
print("b/a: ", result[3])
print(result)