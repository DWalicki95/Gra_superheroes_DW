import random

class SuperPanda:
    def __init__(self, name, superpowers):
        self.name = name
        self.superheroes = superpowers
        self.life_points = random.randint(1,10)

    def attack(self):
        return random.randint(1,10)

    def decrease_life(self, points):
        self.life_points -= points
