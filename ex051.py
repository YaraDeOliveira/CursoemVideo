n = int(input('Digite o valor inicial da PA: '))
r = int(input('Digite a razao da PA:'))
for c in range(0, 10):
    print(f'{n}', end=' -> ')
    n += r
print('FIM')
