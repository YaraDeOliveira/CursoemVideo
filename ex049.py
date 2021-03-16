r = 0
n = int(input('Tabuada de qual numero vc quer saber: '))
for c in range(0, 11):
    r = c*n
    print(f'{n}X{c}={r}')
print('Fim')