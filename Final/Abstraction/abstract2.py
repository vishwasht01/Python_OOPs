from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod ##Every subclass must implement this method, but I’m not defining how.
                    ##It catches the error at class creation time,not later during execution.
    def area(self):
        pass  # abstract method

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

circle = Circle(5)
print(circle.area())
## you cannot create an object of Shape(abstract class)
##You can only create objects of concrete subclasses that implement the abstract method.
##Without @abstractmethod, developers might forget to follow that rule.
##With @abstractmethod, Python enforces it — like a referee making sure every player follows the rules.

