# Atrybuty:
# # # # name – ‘superman’
# # # # superpowers – lista supermocy np [‘ab’, ‘bc’, ‘cd’]
# # # # life_points – randomowa liczba z zakresu 1-10 - biblioteka random (random.randint)
# # # #
# https://docs.python.org/3/library/random.html#random.randint
# random.choice : https://docs.python.org/3/library/random.html#random.choice
# # #
# # # # Metody:
# # # # attack – return randomowa liczba z zakresu 1-10
# # # # decrease_life  - obniża liczbe punktów życia o podaną ilość
# # # # (x wchodzi jako parameter do funkcji: def decrease_life(self, x) )
# # #
# # # # Tworze obiekt poprzez: superman = Superman()
# import superman from zadanie_superheroes
#
import random
from SuperHero import SuperHero

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


