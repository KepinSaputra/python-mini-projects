from main import Game


class Monster(Game):
    def __init__(self, health, energy, side="monster"):
        super().__init__(health, energy, side)
        self.damage = 20

    def monster_attack(self):
        print(f"Monster Attack!!")
        return self.health < 300


m1 = Monster(health=300, energy=100)
