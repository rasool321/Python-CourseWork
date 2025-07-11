l = 'aeiouAEIOU'
n = input("Enter the character/letter:")
if n not in l:
    print(f"{n} is constant")
else:
    print(f'{n} is vowel')