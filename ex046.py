from time import sleep
import emoji
print('\033[1;32m-=\033[m'*20)
print('\033[1;33mCONTAGEM REGRESSIVA')
for c in range(10, -1, -1):
    print(c)
    sleep(1)
print(emoji.emojize('BOOOMMMM :tada: :confetti_ball:', use_aliases=True))
