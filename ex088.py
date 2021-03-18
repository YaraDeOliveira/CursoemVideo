from random import randint
from time import sleep
palpite = list()
print('-'*40)
print(f'{"PALPITE MEGA SENA":^40}')
print('-'*40)
jogos = int(input('Quantos jogos vc quer que eu sorteie? '))
print(f'-=-=-= SORTEANDO  {jogos} JOGOS -=-=-=- ')
for c in range(1, jogos+1):
    for n in range(0, 6):
        s = randint(1, 60)
        while s in palpite:
            s = randint(1, 60)
        if s not in palpite:
            palpite.append(s)
    print(f' Jogo {c}: {sorted(palpite)}')
    palpite.clear()
    sleep(0.5)
print(f'{"BOA SORTE":=^35}')