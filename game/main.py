class Character:
    def __init__(self, health, attack):
        self.health = health
        self.attack = attack


class Player(Character):
    def __init__(self, name):
        self.health = 100
        self.attack = 75
        self.defence = 10
        self.name = name
        super().__init__(self.health, self.attack)

    def change_player_health(self, change):
        self.health = self.health - change
        return self.health


class Friend(Character):
    def __init__(self):
        self.health = 50
        self.attack = 25
        self.defence = 5
        super().__init__(self.health, self.attack)


class Enemy:
    def __init__(self, enemy_name, health, attack):
        self.enemy_name = enemy_name
        self.health = health
        self.attack = attack

    def show_health(self):
        return (self.health)
    def show_attack(self):
        return (self.attack)


zombie_hoard = Enemy("zombie_hoard", 75, 25)
zombie = Enemy("zombie", 25, 15)
zombie_assassin = ("zombie_assassin", 10, 75)
bandit = Enemy("bandit", 100, 20)

