n = '!, @, #, $, %, ^, &, *, (, ), -, _, =, +, \, |,, {, }, ;, :, /, ?, . , >'
m = input("Enter the letter/char:")
if m in n:
    print(f"{m} is a special char..")
else:
    print(f"{m} is not a special char")