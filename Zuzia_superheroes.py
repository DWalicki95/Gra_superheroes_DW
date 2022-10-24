import random

class SuperWieloryb:
    def __init__(self, name, superpowers, life_points):
        self.name = name
        self.superpowers = superpowers
        self.life_points = random.randint(1,10)

    def introduce(self):
        print(f'My name is {self.name} and I have {self.life_points} life points. My superpowers are {self.superpowers}.')
    def attack(self):
        return random.randint(1,10)

    def decrease_life(self, points):
        self.life_points -= pionts

super_wieloryb_zuzi = SuperWieloryb('Super_wieloryb', ['chlust płetwą', 'fala uderzeniowa'], 10)
print(super_wieloryb_zuzi.superpowers)
print(super_wieloryb_zuzi.life_points)
