from time import sleep


def contador(a, b, c):
    print('-' * 40)
    if c == 0:
        c = 1
    if b > a and c < 0:
        c = -c
    if b < a or c < 0:
        if c > 0 and b < a:
            c = -c
        print(f'Contagem de {a} ate {b} em {-c} em {-c}')
        for d in range(a, b - 1, c):
            print(d, end=' ')
            sleep(.5)
        print('Fim!')
    else:
        print(f'Contagem de {a} ate {b} em {c} em {c}')
        for d in range(a, b + 1, c):
            print(d, end=' ')
            sleep(.5)
        print('Fim!')


contador(1, 10, 1)
contador(10, 0, -2)
print('Agora eh a sua vez de personalizar a contagem!')
m = int(input('Inicio:'))
n = int(input('Fim: '))
o = int(input('Passo: '))
contador(m, n, o)
