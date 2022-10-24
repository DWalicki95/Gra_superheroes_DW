import random
class SuperHero():
    def __init__(self, name, superpowers):
        self.name = name
        self.superpowers = superpowers
        self.life_points = random.randint(1, 10)

    def say_hello(self):
        print(f"I am {self.name} I am {self.superpowers} points {self.life_points}")

    def attack(self):
        rand = random.randint(1, 10)
        print(f"{self.name} will attack with power {rand}")
        return rand

    def decrease_life(self, points):
        print(f"{self.name} has {self.life_points} and attacked with {points}.")
        self.life_points = self.life_points - points
        if self.life_points <= 0:
            self.life_points = 0
            print(f"{self.name} dies.")
            print(f"--- GAME OVER ---")


def main(name):
    panda  = SuperHero("Panda", ['ice', 'fire'])
    turtle = SuperHero("Turtle", ['ice', 'fire', 'wind'])

    panda.say_hello()
    turtle.say_hello()
    turtle.decrease_life(panda.attack())


    panda.say_hello()
    turtle.say_hello()


if __name__ == '__main__':
    main('PyCharm')


