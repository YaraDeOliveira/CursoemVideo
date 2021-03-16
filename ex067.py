#print("\033[1;32m{:=^30}\033[m".format('TABUADA'))
print(f"\033[1;32m{'TABUADA':=^30}\033[m")
while True:
    c = 0
    print('-' * 30)
    n = int(input('Tabuada do numero: '))
    print('-' * 30)
    if n < 0:
        break
    while c <= 10:
        print(f'{n} x {c} = {n*c}')
        c += 1
print('FIM DO PROGRAMA')








