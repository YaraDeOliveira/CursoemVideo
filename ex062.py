n = int(input('Digite o valor inicial da PA: '))
r = int(input('Digite a razao da PA:'))
x = n + (10-1)*r
z = 1
while z != 0:
    while n <= x:
        print(f'{n}', end=' -> ')
        n += r
    z = int(input('\nDigite ate qual posicao vc deseja ver:'))
    x = n + (z - 1) * r
print('FIM')