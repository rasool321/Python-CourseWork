#Hybrid Inheritance.
#Multiple subclasses inherit from a single superclass.
class A:
   def display_a(self):
      print("parent class A")

class B(A):
   def display_b(self):
      print('Child class B ')

class C(A):
   def display_c(self):
      print('Child class C ')

class D(B,C):
   def display_d(self):
      print('Child class A,B,C->D ')
'''
class D(A):
   def display_d(self):
      print('Child class A,B,C->D ')
'''

d=D()

d.display_a()
d.display_d()
d.display_b()
d.display_c()

c=C()
c.display_a()
c.display_a()

b=B()
b.display_a()
b.display_b()

a=A()
a.display_a()