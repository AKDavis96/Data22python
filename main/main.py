class Character:
    def __init__(self, health, attack):
        self.health = health
        self.attack = attack


##Survivor
class Survivor(Character):
    def __init__(self, defence):
        self.defence = defence


class Player(Survivor):
    def __init__(self, name):
        self.health = 100
        self.attack = 75
        self.defence = 10
        self.name = name

    def change_player_health(self, change):
        self.health = self.health - change
        return self.health


class Friend(Survivor):
    def __init__(self):
        self.health = 50
        self.attack = 25
        self.defence = 5


# Enemy
class Enemy(Character):
    pass


class Zombie_Hoard(Enemy):
    health = 125
    attack = 25


class Zombie_assasin(Enemy):
    def __init__(self):
        self.health = 5
        self.attack = 75
