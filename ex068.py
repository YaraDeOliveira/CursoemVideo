print(f"\033[1;34m{'PAR OU IMPAR':=^40}\033[m")
print('-='*30)
print('Vamos jogar par ou impar!')
from random import randint
c = 0
while True:
    pcn = randint(0, 20)
    player = int(input('Digite um numero:'))
    total = pcn + player
    if total % 2 == 0:
        esc = 'P'
        esc2 = 'PAR'
    else:
        esc = 'I'
        esc2 = 'IMPAR'
    escolha = str(input('PAR ou IMPAR [P/I]')).upper().strip()[0]
    if escolha == esc:
        print('VOCE VENCEU')
        print(f'Voce jogou {player} e o computador {pcn}.Total de {total}. Deu {esc2}')
        c += 1
    else:
        print('VOCE PERDEU')
        print(f'Voce jogou {player} e o computador {pcn}.Total de {total}. Deu {esc2}')
        break
print(f'Voce ganhou {c} vez(es)!!')
print(f'GAME OVER')
