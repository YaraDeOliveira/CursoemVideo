from random import randint
from time import sleep
numeros = []


def sorteia():
    print(f'Sorteando 5 valores da lista: ', end='')
    for c in range(0, 5):
        z = randint(0, 10)
        print(z, end=' ')
        sleep(0.3)
        numeros.append(z)
    print('Pronto!')


def somaPar(*num):
    s = 0
    for c, v in enumerate(numeros):
        if v % 2 == 0:
            s += v
    print(f'Somando os valores pares de {numeros} temos {s}')


sorteia()
somaPar(numeros)
