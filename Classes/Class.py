class Dog:

    animal_kind = "Dolphin"  # class variable

    def bark(self):  # method (a function in a class)
        return "woof"

# print(Dog().animal_kind)
# print(Dog().bark())          with brackets you have instantiated it
# print(Dog())
# print(Dog.bark)              prints memory location

Myles = Dog()
Oscar = Dog()

print(type(Myles))
print(type(Oscar))

print(Oscar.animal_kind)
print(Myles.animal_kind)

print(Myles.bark())
print(Oscar.bark())

Oscar.animal_kind = "Big Dog"
print(Oscar.animal_kind)
print(Myles.animal_kind)

