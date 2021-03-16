s = c = 0
while True:
    n = int(input('Digite um numero [Digite 999 para parar]:'))
    if n == 999:
        break
    else:
        s += n
        c += 1
print(f'Foram digitados {c} e a soma entre eles eh {s}')

