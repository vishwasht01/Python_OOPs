##Multiple Level
class A:
    def f1(self):
        print("A feature")
class B:
    def f2(self):
        print("B feature")
class C(A, B):
    def f3(self):
        print("C feature")

obj = C()
obj.f1()
obj.f2()
