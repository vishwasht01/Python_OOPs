##Compile-time polymorphism

class Vector:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def __add__(self,other):
        if isinstance(other,Vector):
            return Vector(self.x+other.x,self.y+other.y)

    def __str__(self):
        return f"({self.x},{self.y})"

v1 = Vector(5,7)
v2 = Vector(9,8)
print(v1+v2)
