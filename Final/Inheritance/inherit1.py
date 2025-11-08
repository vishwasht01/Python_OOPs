#Single Inheritance
class A:
    def feature1(self):
        print("Feature 1")
class B(A):
    def feature2(self):
        print("Feature 2")

obj = B()
obj.feature1()
obj.feature2()
