def generate(strings, x=2, flag=True):
    result = list()
    for word in strings:
        temp = list()
        for i in range(len(word)):
            if flag and ord(word[i]) % x == 0:
                temp.append(word[i])
            elif not flag and ord(word[i]) % x != 0:
                temp.append(word[i])
        result.append(temp)
    return result


print(generate(["test", "hello", "lab002"], 2, False))
