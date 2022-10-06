vowels = "aeiouAEIOU"

def is_vowel(char):
    return char in vowels


string = input("Enter a string: ")
counter = 0
for letter in string:
    if is_vowel(letter): 
        counter+=1
print("Total vowels in input string: ", counter)