n = int(input('Digite o valor inicial da PA: '))
r = int(input('Digite a razao da PA:'))
x = n + (10-1)*r
while n <= x:
    print(f'{n}', end=' -> ')
    n += r
print('FIM')
