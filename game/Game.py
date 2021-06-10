import main
import random
import encounter


def enemy_selection(num):
    if num < 0.25:
        return main.zombie_hoard
    elif num < 0.5:
        return main.zombie
    elif num < 0.75:
        return main.zombie_assassin
    else:
        return main.bandit

def item_chosen(item):
    if item == "shield":
        player.defence += encounter.shield.defence
    elif item == "shotgun":
        player.attack += encounter.shotgun.attack
    elif item == "defence potion":
        player.health += encounter.defence_potion.health
        player.defence += encounter.defence_potion.defence
    else:
        player.health += encounter.bandage.health



name = input(f"Please enter your character name ")
player = main.Player(name)
print(f"Hi {name}! Your health is {player.health}, attack is {player.attack} and defence is {player.defence}")
start_item = input("You may choose on of the following to aid you in battle, a shield or a shotgun  ")
item_chosen(start_item)
print(f"Now your health is {player.health}, attack is {player.attack} and defence is {player.defence}")
item_chosen(start_item)
enemy1 = enemy_selection(random.random())
print(f"Oh no you run into a {enemy1.enemy_name}!!")
print(f"The {enemy1.enemy_name} has an attack rating of {main.Enemy.show_attack(enemy1)} and total health of {main.Enemy.show_health(enemy1)}")
run = input("Would you like to run or fight? ")
main.Player.change_player_health(player, enemy1.attack)
print(player.health)
