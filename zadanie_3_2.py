# stwórz grę w stylu mortal-combat, gdzie zawodnikami będa
# obiekty naszych klas (czyli np hero = Superhero()).
# W każdej rundzie losowane maja być dwie postacie
# (dwóch superbohaterów, czyli dwa obiekty). Każdy z nich może walczyć
# losową bronią z superpowers (należy ja wylosować) oraz zadać losową
# ilość punktów obrażeń z zakresu 1-10 (funkcja attack).
# Ten gracz, który wylosuje większą ilość obrażeń, obniża life_points
# przeciwnikowi o swoją liczbę obrażeń minus liczba którą wylosował przeciwnik
# np	gracz S1 zadaje 5 punków obrażeń,	gracz S2 zadaje 6 punków obrażeń
# => w efekcie wygrywa gracz S2 i zadaje 1 (czyli 6 minus 5) punkty obrażeń.
# Po ataku należy zaktualizować liczbę punktów życia przegranego.
# Jeśli wyniesie ona <=0 gracz taki odpada z gry. Gra trwa do momentu,
# gdy zostanie ostatni gracz (on oczywiście wygrywa;-) ).
# Jeśli dwóch graczy zada takie same obrażenia, nikt nie odnosi obrażeń i
# odbywa się ponowne losowanie dwóch graczy


import random

from tets_oliwii import SuperPanda
from tets_szymona import SuperZaba
from Zuzia_superheroes import super_wieloryb_zuzi
from test_dawida import SuperPajak
from adams_superhero import superMan
from branch_pd import superman
from superhydra import super_hydra1

