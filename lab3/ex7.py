def set_operations(*sets):
    result = {}
    for i in range(len(sets)):
        for j in range(len(sets)):
            if j != i:
                a = sets[i]
                b = sets[j]
                intersection = str(a) + "|" + str(b)
                union = str(a) + "&" + str(b)
                a_minus = str(a) + "/" + str(b)
                b_minus = str(b) + "/" + str(a)
                result[intersection] = set(a).intersection(b)
                result[union] = set().union(a, b)
                result[a_minus] = set(a).difference(b)
                result[b_minus] = set(b).difference(a)
    return result

print(set_operations({1,2}, {2, 3}))