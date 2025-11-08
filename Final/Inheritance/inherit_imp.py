class Person:
    def __init__(self, *args, name=None, **kwargs):
        self.name = name or "Unknown"
        print("Person init:", self.name)
        super().__init__(*args, **kwargs)

class SalaryMixin:
    def __init__(self, *args, salary=0, **kwargs):
        self.salary = salary
        print("SalaryMixin init:", self.salary)
        super().__init__(*args, **kwargs)

class LoggerMixin:
    def __init__(self, *args, log_prefix='', **kwargs):
        self.log_prefix = log_prefix
        print("LoggerMixin init:", self.log_prefix)
        super().__init__(*args, **kwargs)

class Employee(LoggerMixin, SalaryMixin, Person):
    def __init__(self, *args, **kwargs):
        print("Employee init start")
        super().__init__(*args, **kwargs)
        print("Employee init end")

alice = Employee(name="Alice", salary=1000, log_prefix="[ALICE] ")
##In multiple inheritance, every class should accept *args and **kwargs and call super().__init__(*args, **kwargs)
# so that all classes in the MRO chain get initialized properly.