from Animal import Animal

class Reptile(Animal):

    def __init__(self):
        super().__init__()
        self.cold_blooded = True
        self.tetrapod = None
        self.heart_chambers = [3, 4]
        self.amniotic_eggs = None

    def seek_heat(self):
        print("It's chilly outside where is the sun?")

    def hunt(self):
        print("wiat for it, pounce!!")

    def use_venom(self):
        print("I will use it")

    def attract_mate(self):
        print("Time to attract mate")

jeremy = Reptile()
jeremy.breathe()