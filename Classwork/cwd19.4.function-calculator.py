def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
def mod(a,b):
    return a%b

exp = input('Enter the expression: ')
op=None
for i in exp:
    if not i.isdigit():
        op=i
        break
a,b = exp.split(op)
a,b=int(a),int(b)
if op=='+':
    print(add(a,b))
elif op=='-':
    print(sub(a,b))
elif op=='*':
    print(mul(a,b))
elif op=='/':
    print(div(a,b))
elif op=='%':
    print(mod(a,b))


