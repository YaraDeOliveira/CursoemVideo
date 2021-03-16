s = 0
d = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        d = d + 1
        s += c
print(f'A soma entre os {d} num impares que sejam div por 3 eh \033[35m{s}')
