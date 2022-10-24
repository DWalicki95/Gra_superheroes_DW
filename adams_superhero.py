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
import random as rd


class SuperHero:
    """
    This is class to defining superheros
    """

    def __init__(self, nazwa: str, moce: list[str]):
        self.name = nazwa
        self.superpowers = moce
        self.life_points = rd.randint(1, 10)

    def attack(self):
        return rd.randint(1, 10)

    def decrease_life(self, take_hit: int):
        self.life_points -= take_hit


