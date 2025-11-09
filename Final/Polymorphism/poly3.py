##You can redefine (override) a static method in a subclass —
##but remember: Python will just replace the version in the subclass namespace.

class Currency:
    @staticmethod
    def get_symbol():
        return "Generic Currency"

class Dollar(Currency):
    @staticmethod
    def get_symbol():
        return "$"

class Euro(Currency):
    @staticmethod
    def get_symbol():
        return "€"

print(Currency.get_symbol())
print(Dollar.get_symbol())
print(Euro.get_symbol())
