class Employee:
    def __init__(self, first_name, last_name, maritual, age, id):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__maritual = maritual
        self.__age = age
        self.__id = id

    def getLast_name(self):
        print(self.__last_name)

    def setLast_name(self, last_name):
        if self.__maritual == "married":
            self.__last_name = last_name
            print(f"have a great honey moon Mr/Mrs {self.__last_name}")
        else:
            print("You can't change your name if you are not married")

    def setAge(self):
        birthday = input(f"what month is your birthday? ")
        if birthday.lower() == "may":
            self.__age += 1
            print(self.__age)
        else:
            print(f"have a nice birthday in the future")

    def getAge(self):
        print(self.__age)

    def getid(self):
        print(self.__id)

    def setid(self):
        self.__id = self.__id[0:-1] + self.__maritual[0]

    def getMaritual(self):
        print(self.__maritual)

    def setMaritual(self, status):
        self.__maritual = status
        self.setid()

    def getAll(self):
        self.getLast_name()
        self.getMaritual()
        self.getAge()
        self.getid()


Dave = Employee("Dave", "Jeff", "married", 23, "123s")
Matt = Employee("matt", "brack", "single", 25, "456s")

Matt.getAll()
Matt.setLast_name("brackenbury")
Matt.setMaritual("married")
Matt.setLast_name("rothwell")
Matt.setAge()
Dave.setid()
Dave.getAll()

Matt.getAll()
