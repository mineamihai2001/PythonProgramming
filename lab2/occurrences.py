def occurrences(lists, x):
    result = []
    freq = {}
    for list in lists:
        for item in list:
            try:
                freq[item] +=1
            except:
                freq[item] = 1
    for key, value in freq.items():
        if value == x:
            result.append(key)
    return result


test = [1, 2, 3], [2, 3, 4], [4, 5, 6], [4, 1, "test"]
print(occurrences(test, 2))
