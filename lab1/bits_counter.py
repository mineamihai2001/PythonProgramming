def binary(n):
    return bin(n)[2:]

number = int(input("decimal number: "))
print(str(binary(number)).count("1"))