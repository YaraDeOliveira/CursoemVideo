matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somapar = terc = maior = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = (int(input(f'Digite um valor para [{l} , {c}]:')))
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
        if matriz[l][c] % 2 == 0:
            somapar += matriz[l][c]
        if c == 2:
            terc += matriz[l][c]
        if l == 1 and c == 0:
            maior = matriz[l][c]
        if l == 1 and matriz[l][c] > maior:
            maior = matriz[l][c]
    print()
print('-='*40)
print(f'A soma dos valores pares eh {somapar}')
print(f'A soma dos valores da terceira coluna eh {terc}')
print(f'O maior valor da segunda linha eh {maior}')
