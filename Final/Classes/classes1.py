class MathTools:
    pi = 3.14

    def area_circle(self, r):
        return self.pi * r * r

    @classmethod
    def describe(cls):
        return f"Pi value = {cls.pi}"

    @staticmethod
    def add(a, b):
        return a + b

math = MathTools()
print(math.describe())
print(math.area_circle(9))
print(math.add(2,5))
