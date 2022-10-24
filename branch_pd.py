import random
class Superman():
    def __init__(self, name, superpowers):
        self.name = name
        self.superheroes = superpowers
        self.life_points = random.randint(1,10)
    def attack(self):
        return random.randint(1,10)
    def decrease_life(self, decrease):
        self.life_points -= decrease
