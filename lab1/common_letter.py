from string import ascii_letters

def common_letter(string):
    max = -1
    common = ""
    for letter in ascii_letters:
        count = string.count(letter)
        if count > max:
            max = count
            common = letter
    return max

print(common_letter("an apple is not a tomato"))