from main import Game
from monster import *

player_name = input("Input Your Name: ")
player_health = int(input("How Much Health Would You Like to Have?: "))


class Player(Game):
    def __init__(self, health, energy, name, side="player"):
        super().__init__(health, energy, side)
        self.name = name
        print(f"Player {player_name} has been Created")

    def player_attack(self, target, damage):
        target.health -= damage * 2
        self.energy -= damage
        self.damage = damage
        print(f"{self.name} Attack With {self.damage}")
        if target.monster_attack():
            self.health -= target.damage
            target.energy -= target.damage


p1 = Player(health=player_health, energy=100, name=player_name)

wouldAttack = input(
    f"A Monster Arrived!! It Has {m1.health} Health!! Would You like to Attack?[Y/N]: "
).lower()

while p1.health > 0:
    if wouldAttack == "y":
        p1.player_attack(m1, damage=20)
        m1.profile()
        p1.profile()
        wouldAttack = input("Attack again?[Y/N] ").lower()
        if p1.health <= 0:
            print("You Died! Thank You for Playing")
        if m1.health <= 0:
            print("Monster has been Defeated")
    else:
        print("You've Lost! Thankss")
        break
