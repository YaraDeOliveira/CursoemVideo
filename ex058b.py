print('\033[1;33m{:=^40}\033[m'.format('JOGO DE ADIVINHACAO'))
from random import randint
from time import sleep
pc = randint(0, 10)
acertou = False
tenta = 0
while not acertou:
    player = int(input('Digite um numero entre 0 e 10:'))
    sleep(1)
    tenta += 1
    if player == pc:
        acertou = True
    else:
        if pc > player:
            print('\033[1;31mMais... Tente novamente!\033[m')
        else:
            print('\033[1;31mMenos... Tente novamente!\033[m')
print(f'\033[1;34mVOCE ACERTOU!!! VOCE PRECISOU DE {tenta} TENTATIVAS')