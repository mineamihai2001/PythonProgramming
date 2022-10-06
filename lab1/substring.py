string1 = input("String to search in: ")
string2 = input("String to search: ")


def find_index(string1, string2, start):
    try:
        print('here', string1.index(string2, start))
        return True
    except:
        print("No more...")
        return False


step = len(string2)
end = len(string2)
first_index = find_index(string1, string2, 0)

if first_index == False:
    exit

start = first_index + step
counter = 1
index_start = start

for i in range(start, end):
    if find_index(string1, string2, index_start) == True:
        counter += 1
        index_start += step

print("Total occurrences: ", counter)
