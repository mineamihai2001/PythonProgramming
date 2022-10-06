def is_triange(arr):
    ip = max(arr)
    arr.remove(ip)
    return True if arr[0] + arr[1] > ip else False

a = input('a: ')
b = input('b: ')
c = input('c: ')
print(is_triange([a, b, c]))