'''n1 = int(input('Digite o numero:'))
fat = 1
for x in range(n1-1, 0, -1):
    print(x, fat)
    fat += fat * x
    print(fat)
print(f'O fatoral eh {fat}')'''

"""n1 = int(input('Digite o numero:'))
aux = n1-1
fat = 1
while n1 > 1:
    fat += (fat * aux)
    n1 = (n1 - 1)
    aux = n1 - 1
    print(n1, aux)
print(f'O fatoral eh {fat}')"""

'''from math import factorial
n = int(input('Digite um numero:'))
f = factorial(n)
print('O fatorial de {} eh {}'.format(n, f))'''

n = int(input('Digite um numero:'))
c = n
f = 1
print('Calculando {}! = '.format(n), end='')
while c > 0:
    print(f'{c}', end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print(f)
