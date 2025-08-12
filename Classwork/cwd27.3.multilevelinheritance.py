#Multilevel Inheritance.
#A subclass inherits from a class which itself is a subclass of another class.
class A:
   def display_a(self):
      print("parent class A")

class B(A):
   def display_b(self):
      print('Child class B ')

class C(B):
   def display_c(self):
      print('Child class C ')

class D(C):
   def display_d(self):
      print('Child class A,B,C->D ')

d=D()

d.display_a()
d.display_b()
d.display_c()
d.display_d()
