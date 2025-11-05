"""
Full demo: polymorphism traps, duck typing, operator overloading,
MRO and cooperative init, using alice and bob.
"""

# ------------------------------
# 1. Method overriding (traditional polymorphism)
# ------------------------------

class Person:
    def speak(self):
        print("Person speaking")

class Student(Person):
    def speak(self):
        print("Student speaking")

print("=== 1. Method overriding ===")
alice = Person()
bob = Student()

for p in [alice, bob]:
    p.speak()  # Runtime decides which method to call
print()


# ------------------------------
# 2. Duck typing failure
# ------------------------------

class Dog:
    def speak(self):
        return "Woof"

class Cat:
    def speak(self, times):   # incompatible signature
        return "Meow " * times

print("=== 2. Duck typing failure ===")
animals = [Dog(), Cat()]
for a in animals:
    try:
        print(a.speak())  # Works for Dog, fails for Cat
    except TypeError as e:
        print("Error:", e)
print()


# ------------------------------
# 3. Operator overloading + NotImplemented fallback
# ------------------------------

class NumberBox:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        if isinstance(other, NumberBox):
            return NumberBox(self.value + other.value)
        return NotImplemented

    def __radd__(self, other):
        # handle reversed addition
        if isinstance(other, int):
            return NumberBox(self.value + other)
        return NotImplemented

    def __repr__(self):
        return f"NumberBox({self.value})"

print("=== 3. Operator overloading ===")
x = NumberBox(10)
y = NumberBox(5)

print("x + y =", x + y)      # calls __add__
print("3 + x =", 3 + x)      # triggers __radd__
##print("x + 3 =", x + 3)      # also works because __radd__ handles it
print()


# ------------------------------
# 4. MRO effects (diamond inheritance)
# ------------------------------

class A:
    def greet(self): print("A.greet")

class B(A):
    def greet(self): print("B.greet")

class C(A):
    def greet(self): print("C.greet")

class D(B, C):  # diamond
    pass

print("=== 4. MRO diamond ===")
d = D()
d.greet()  # Follows MRO: D → B → C → A
print("MRO:", [cls.__name__ for cls in D.mro()])
print()


# ------------------------------
# 5. Cooperative vs non-cooperative __init__
# ------------------------------

print("=== 5. Cooperative vs Non-cooperative init ===")

class Base:
    def __init__(self, base_arg, **kwargs):
        print("Base init with:", base_arg)
        super().__init__(**kwargs)

class CooperativeMixin:
    def __init__(self, **kwargs):
        print("CooperativeMixin init")
        super().__init__(**kwargs)

class NonCooperativeMixin:
    def __init__(self):
        print("NonCooperativeMixin init")
        # no **kwargs, breaks the chain
        super().__init__()

print("-- Cooperative --")
class GoodChild(Base, CooperativeMixin):
    def __init__(self, **kwargs):
        print("GoodChild init")
        super().__init__(**kwargs)

gc = GoodChild(base_arg="hello")

print("\n-- Non-Cooperative --")
try:
    class BadChild(Base, NonCooperativeMixin):
        def __init__(self, **kwargs):
            print("BadChild init")
            super().__init__(**kwargs)

    bc = BadChild(base_arg="oops")  # will fail
except TypeError as e:
    print("Error:", e)
