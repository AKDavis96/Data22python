class Dog:

    def __init__(self, name, colour):  # remember to always specify self
        self.animal_kind = "canine"
        self.name = name
        self.colour = colour
        self.bark()

    def bark(self):
        return "woof"


Amy = Dog("Amy", "Golden")

print(Amy.name)
print(Amy.colour)
print(Amy.animal_kind)
print(Amy.bark())