#import operators
import operators as opr
#from operators import *
#from operators import add,sub,mul,div,mod,exp
a=int(input("Enter the value for a:"))
b=int(input("Enter the value for b:"))
op=input("Enter the a operator(+-*/%**):")
if op=='+':
    opr.add(a,b)
elif op=='-':
    opr.sub(a,b)
elif op=='*':
    opr.mul(a,b)
elif op=='/':
    opr.div(a,b)
elif op=='%':
    opr.mod(a,b)
elif op=='**':
    opr.exp(a,b)