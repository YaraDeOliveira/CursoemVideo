x = 0
n = int(input('Digite um numero:'))
for c in range(1, n+1):
    if n % c == 0:
        x += 1
        print(f'\033[33m{c}', end=' ')
    else:
        print(f'\033[31m{c}', end=' ')
print(f'\n\033[mO numero {n} foi divisivel {x} vezes')
if x == 2:
    print('E por isso ele E PRIMO')
else:
    print('E por isso ele NAO E PRIMO')
