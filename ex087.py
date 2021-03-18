matriz = list()
soma = terc = maior = 0
for l in range(0, 3):
    for c in range(0, 3):
        n = int(input(f'Digite um valor para [{l} , {c}]:'))
        matriz.append(n)
        if n % 2 == 0:
            soma += n
        if c == 2:
            terc += n
        if l == 1:
            maior = n
        if l == 1 and n > maior:
            maior = n
print('-='*40)
print(f'[ {matriz[0]} ] [ {matriz[1]} ] [ {matriz[2]} ]')
print(f'[ {matriz[3]} ] [ {matriz[4]} ] [ {matriz[5]} ]')
print(f'[ {matriz[6]} ] [ {matriz[7]} ] [ {matriz[8]} ]')
print('-='*40)
print(f'A soma dos valores pares eh {soma}')
print(f'A soma dos valores da terceira coluna eh {terc}')
print(f'O maior valor da segunda linha eh {maior}')