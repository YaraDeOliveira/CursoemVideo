from time import sleep


def maior(*num):
    print('Analisando os valores passados...')
    sleep(1)
    for c in num:
        print(c, end=' ')
        sleep(.3)
    print(f'Foram passados {len(num)} valores ao todo.')
    print(f'O maior numero informado foi o {max(num)}.')
    print('-='*30)


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior(0)


