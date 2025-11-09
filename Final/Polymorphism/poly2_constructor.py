##If the parent’s constructor calls an overridden method,
##make sure any subclass attributes that the overridden method uses are initialized before calling super().__init__().

class Parent:
    def __init__(self):
        print("Parent constructor")
        self.greet()   # 👈 overridden method

    def greet(self):
        print("Parent greet")

class Child(Parent):
    def __init__(self):
        self.name = "Alice"
        super().__init__()

    def greet(self):
        print(f"Hello from Child, {self.name}")

Child()
##Constructors can’t be virtual because the derived object doesn’t exist when the base constructor runs.
# In Python, methods are always virtual, so if a base constructor calls an overridden method,
# the child’s version runs — but this is unsafe because the child object isn’t fully initialized yet.
##Python does not restrict calling overridden methods from constructors —
##because it uses dynamic binding everywhere.