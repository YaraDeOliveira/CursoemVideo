import random
import emoji
print(emoji.emojize(' '*10 + '\033[1;36;43m:game_die:JOKENPO:video_game:\033[m'))
print('--=--'*10)
pc = random.randint(1, 3)
player = int(input('ESCOLHA:\n(1): PEDRA\n(2)PAPEL OU\n(3) TESOURA: '))
if pc == player:
    print(emoji.emojize('EMPATE:expressionless:',use_aliases=True))
elif pc == 1 and player == 3 or pc == 2 and player == 1 or pc == 3 and player == 2:
    print('VOCE PERDEU')
else:
    print('VOCE GANHOU')