import random


class SuperHydra:
    def __init__(self, name, superpowers):
        self.name = name
        self.superpowers = superpowers
        self.life_points = random.randint(1, 10)

    def attack(self):
        return random.randint(1,10)

    def decrease_life(self, life_points):
        self.life_points -= life_points


super_hydra1 = SuperHydra('Hydralisk', ['spikes', 'acid'])
