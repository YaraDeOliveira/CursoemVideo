geral = list()
par = list()
impar = list()
for c in range(1, 8):
    n = int(input(f"Digite o {c} numero: "))
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)
geral.append(par[:])
geral.append(impar[:])
print(f'Os valores pares digitados foram {sorted(geral[0])}')
print(f'Os valores impares digitados foram {sorted(geral[1])} ')