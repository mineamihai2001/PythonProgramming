def equals(dictionary1, dictionary2):
    for i in dictionary1:
        if dictionary1[i] not in dictionary2.values() or i not in dictionary2:
            return False

    for item in dictionary2:
        if dictionary2[item] not in dictionary1.values() or item not in dictionary1:
            return False

    return True


dictionary1 = {1: 11, 2: "abc", 3: 12, 4: [1, 2, 3, 4]}
dictionary2 = {'a': 11, 'b': "abc", 'c': [1, 2, 3, 4], 'd': 12}

print(equals(dictionary1, dictionary2))
print(equals(dictionary1, dictionary1))
