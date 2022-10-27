def list(l):
    uniqueElements = set(l)
    for element in uniqueElements:
        for i in range(0, len(l)):
            if element == l[i]:
                l.remove(element)
                break
    return (len(set(uniqueElements-set(l))), len(set(l)))


print(list([1, 1, 3, 4, 5, 2, 2, 3, 6, 7, 8]))
