def is_palindrome(x):
    y = 0
    cx = x
    while x > 0:
        y = y * 10 + x % 10
        x = x // 10
    return True if cx == y else False


x = int(input())
print(is_palindrome(x))
