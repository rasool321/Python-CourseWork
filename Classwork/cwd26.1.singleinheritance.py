#One subclass inherits from one superclass.
class A:
   def display_a(self):
      print("parent class A")

class B(A):
   def display_b(self):
      print('Child class B (B<-A)')
a=A()
a.display_a()
b=B()
b.display_b()
b.display_a()