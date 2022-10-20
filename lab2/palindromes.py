def is_palindrome(number):
    copy = number
    r = 0
    while copy > 1:
        r = r * 10 + copy % 10
        copy //= 10
    return True if r == number else False


def palindromes(numbers):
    _list = list()
    for number in numbers:
        if is_palindrome(number) == True:
            _list.append(number)
    return (len(_list), max(_list))

print(palindromes([123321, 223322, 989, 123, 43819, 777]))                
