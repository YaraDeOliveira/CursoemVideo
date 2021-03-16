print('\033[1;33m{:=^40}\033[m'.format('JOGO DE ADIVINHACAO'))
from random import randint
from time import sleep
pc = randint(0, 10)
player = int(input('Digite um numero entre 0 e 10:'))
tenta = 1
while player != pc:
    sleep(1)
    if pc > player:
        print('\033[1;31mMais... Tente novamente!\033[m')
    else:
        print('\033[1;31mMenos... Tente novamente!\033[m')
    tenta += 1
    player = int(input('Digite um numero entre 0 e 10:'))
print(f'\033[1;34mVOCE ACERTOU!!! VOCE PRECISOU DE {tenta} TENTATIVAS')