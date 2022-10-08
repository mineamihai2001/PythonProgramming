def number_extract(string):
    result = 0
    found = False
    for i in range(len(string)):
        try:
            result = result * 10 + int(string[i])
            found = True
        except:
            if found == True:
                return result
            else:
                continue
    return None


print(number_extract("abc123avc678aaa"))
