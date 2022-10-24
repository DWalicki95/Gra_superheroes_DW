import random

from test_dawida import super_panda_oliwii, super_pajak_dawida
from adams_superhero import superMan
from SH import venom
from superhydra import super_hydra1
from test_ola import superman
from tets_szymona import superZaba1
from Zuzia_superheroes import super_wieloryb_zuzi

superhero_list = [super_panda_oliwii,
                  super_pajak_dawida,
                  superMan,
                  venom,
                  super_hydra1,
                  superman,
                  superZaba1,
                  super_wieloryb_zuzi
                  ]

ans = ''
counter = 1
while (ans == '') & (len(superhero_list) > 1):
    print(f'----------RUNDA {counter}-------------')
    for hero in superhero_list:
        print(hero.name, hero.life_points)
    fighters = random.sample(superhero_list, k=2)
    attack = []
    for fighter in fighters:
        fighter_attack = fighter.attack()
        attack.append(fighter_attack)
        print(
            f'Postać {fighter.name} walczy {random.choice(fighter.superpowers)} i zadaje {fighter_attack} obrazeń')

    if attack[0] > attack[1]:
        attack_points = attack[0] - attack[1]
        print(
            f'Postac {fighters[0].name} wygrywa z {fighters[1].name} zadajac mu {attack_points} obrazen')
        fighters[1].decrease_life(attack_points)
        if fighters[1].life_points <= 0:
            print(f'Postac {fighters[1].name} umiera')
            superhero_list.remove(fighters[1])

    elif attack[0] < attack[1]:
        attack_points = attack[1] - attack[0]
        print(
            f'Postac {fighters[1].name} wygrywa z {fighters[0].name} zadajac mu {attack_points} obrazen')
        fighters[0].decrease_life(attack_points)
        if fighters[0].life_points <= 0:
            print(f'Postac {fighters[0].name} umiera')
            superhero_list.remove(fighters[0])

    else:
        print('REMIS')
        counter += 1
        continue
    counter += 1
    ans = input()

print(f'Wygrywa: {superhero_list[0].name}')
