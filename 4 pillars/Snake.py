from Reptile import Reptile
from Animal import Animal

class Snake(Reptile):

    def __init__(self):
        super().__init__()
        self.forked_tongue = True
        self.venom = None
        self.limbs = False

    def use_tongue_to_smell(self):
        print("do I smell nice, or do I taste nice")

Oscar = Snake()
Oscar.seek_heat()

