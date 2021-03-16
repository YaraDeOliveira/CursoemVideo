import emoji
from random import randint
from time import sleep
itens = ('PEDRA', 'PAPEL', 'TESOURA')
pc = randint(0, 2)
player = int(input('ESCOLHA:\n(0)PEDRA\n(1)PAPEL \n(2)TESOURA \nSUA JOGADA:'))
print('-='*11)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
#print('O pc jogou {}'.format(itens[pc]))
#print('O jogador jogou {}'.format(itens[player]))
if pc == player:
    print(emoji.emojize('EMPATE:expressionless: Vc escolheu {} e o pc escolheu {}'.format(itens[player], itens[player]), use_aliases=True))
elif pc == 'PEDRA' and player == 'TESOURA' or pc == 'PAPEL' and player == 'PEDRA' or pc == 'TESOURA' and player == 'PAPEL':
    print('\033[1;32mVOCE PERDEU!!\033[m Vc escolheu {} e o pc escolheu {}'.format(itens[player], itens[pc]))
else:
    print('\033[1;32mVOCE GANHOU!!\033[m Vc escolheu {} e o pc escolheu {}.'.format(itens[player], itens[pc]))