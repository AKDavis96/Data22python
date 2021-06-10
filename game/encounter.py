##Encounters
class Items:
    def __init__(self, name, health = 0, attack = 0, defence = 0):
        self.name = name
        self.health = health
        self.attack = attack
        self.defence = defence



shield = Items("shield", 0, 0, 15)
shotgun = Items("shotgun", 0, 10, 0)
bandage = Items("bandage", 20, 0, 0)
defence_potion = Items("defence potion", 10, 0, 10)





