import random
import emoji
print(emoji.emojize(' '*10 + '\033[1;36;43m:game_die:JOKENPO:video_game:\033[m'))
print('--=--'*10)
pc = random.choice(['PEDRA', 'PAPEL', 'TESOURA'])
player = str(input('ESCOLHA: PEDRA, PAPEL OU TESOURA: ')).strip().upper()
if pc == player:
    print(emoji.emojize('EMPATE:expressionless:', use_aliases=True))
elif pc == 'PEDRA' and player == 'TESOURA' or pc == 'PAPEL' and player == 'PEDRA' or pc == 'TESOURA' and player == 'PAPEL':
    print('vc escolheu {} e o pc escolheu {}, VOCE PERDEU'.format(player, pc))
else:
    print('vc escolheu {} e o pc escolheu {}, voce ganhou'.format(player, pc))