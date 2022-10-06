from cmath import sqrt

def is_prime(number):
    if number < 2:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False
    for i in range(3, sqrt(number) + 1):
        if number % i == 0:
            return False
    return True

n = int(input("Number: "))
print('is prime' if is_prime(10) == True else 'false') 

