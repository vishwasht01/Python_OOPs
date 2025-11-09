class Base:
    var = "Base"

    @staticmethod
    def static_show():
        print("Static:", Base.var)

    @classmethod
    def class_show(cls):
        print("Class:", cls.var)

class Sub(Base):
    var = "Sub"

Sub.static_show()  # Still prints "Base", because @staticmethod doesn’t know which class called it
Sub.class_show()   # Prints "Sub"
