##Multilevel Inheritance
class A:
    def f1(self):
        print("Feature 1.")

class B(A):
    def f2(self):
        print("Feature 2.")

class C(B):
    def f3(self):
        print("Feature 3.")

obj = C()
obj.f3()