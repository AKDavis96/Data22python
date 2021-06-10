# n = 0.034234
#
# print(f"Fixed point:  {n:f}")
# print(f"Exponential Notation:  {n:e}")

class Dog:
    def __init__(self, age):
        self.age = age

    def __str__(self):
        return f"A {self.age} year old dog"

    def __format__(self, format_spec):
        if format_spec == "dog":
            return f"A {self.age*7} dog years old"
        else:
            return self.__str__()


rover = Dog(5)
print(f"{rover}")
print(f"{rover:dog}")