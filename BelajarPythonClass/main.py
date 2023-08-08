class Game:
    def __init__(self, health, energy, side):
        self.health = health
        self.energy = energy
        self.side = side

    def profile(self):
        print(f"{self.side} have {self.health} health, and {self.energy} energy!")
