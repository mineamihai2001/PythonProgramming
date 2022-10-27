def occurrences(string):
    freq = {}
    for char in string:
        freq[char] = freq[char] + 1 if char in freq else 1
    return freq

print(occurrences("Ana has apples"))