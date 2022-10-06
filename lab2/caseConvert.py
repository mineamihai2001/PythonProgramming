import re

def convert(string):
    list = re.findall("[A-Z][^A-Z]*", string)
    result = []
    for word in list:
        result.append(chr(ord(word[0]) + 32) + word[1:])
    return '_'.join(result)

string = input("String: ")
print(convert(string))