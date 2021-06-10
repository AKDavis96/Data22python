class Person:
    def __init__(self, name, age = 0):
        self._name = name
        self.__age = age

    def display(self):
        print(self._name)  # hides slightly
        print(self.__age)  # can't access this

    def getAge(self):
        print(self.__age)

    def setAge(self, age):
        self.__age = age

Ola = Person("Ola", 75)
Ola._name = "Olaaaaaa"
Ola.__age = 40
Ola.display()

Ola.setAge(30)
Ola.display()

# Ola = Person("Ola", 75)
# Ola.display()
#
# Ola.__age = 50
# Ola.display()
#
# Ola._name = "Olaa"
# Ola.display()
#
# Ola.getAge()
# Ola.setAge(25)
#
# Ola.display()
Ola._name = "Olaaaaaa"

