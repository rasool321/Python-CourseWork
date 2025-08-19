class Number:
    def __init__(self,number):
        self.number=number
    
    def __str__(self):
        return f'{self.number}'

    def __add__(self,other):
        return self.number+other.number
    
    def __sub__(self,other):
        return self.number-other.number
    
    def __mul__(self,other):
        return self.number*other.number
    
    def __truediv__(self,other):
        return self.number/other.number
    
    def __eq__(self,other):
        return self.number==other.number
    
    def __lt__(self,other):
        return self.number<other.number
    
    def __gt__(self,other):
        return self.number>other.number
   
n1=Number(10)
n2=Number(20)
print(f'number: {n2}')
print(f'add : {n1+n2}')
print(f'sub : {n2-n1}')
print(f'mul : {n1*n2}')
print(f'div : {n2/n1}')
print(f'equal : {n1==n2}')
print(f'lessthan : {n1<n2}')
print(f'greaterthan : {n1>n2}')
    