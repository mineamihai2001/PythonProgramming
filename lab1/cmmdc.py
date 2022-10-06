def cmmdc(a, b):
    while (b > 0):
        r = a % b
        a = b
        b = r
    return a


def list_cmmdc(list):
    a = int(list[0])
    for i in range(1, len(list)):
        b = int(list[i])
        a = cmmdc(a, b)
    return a


list = input("Enter a list of numbers: ").split()
result = list_cmmdc(list); 
print("CMMDC: ", result)
