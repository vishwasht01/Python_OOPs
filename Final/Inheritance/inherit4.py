##Python supports Method Overriding but no OverLoading
class Parent:
    def show(self):
        print("Parent show()")

class Child(Parent):
    def show(self):
        print("Child show()")

obj = Child()
obj.show()  # Child show()


class Parent:
    def show(self):
        print("Parent method")

class Child(Parent):
    def show(self):
        super().show()  # calls parent
        print("Child method")

obj = Child()
obj.show()
