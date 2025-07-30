def count_vowel(s):
    l = 'aeiouAEIOU'
    c = 0
    for char in s:
        if char in l:
            c += 1
    return c

s = input("Enter a string: ")
print("Number of vowels:", count_vowel(s))
