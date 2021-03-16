num = []
for c in range(0, 5):
    num.append(int(input(f'Digite um numero para posicao {c}:')))
print(f'Os numeros digitados foram: {num}')
print(f'O maior numero digitado foi {max(num)}, na posicao ', end='')
for c, v in enumerate(num):
    if v == max(num):
        print(c, end=' ')
print(f'\nO menor numero digitado foi {min(num)}, na posicao:', end='')
for x, z in enumerate(num):
    if z == min(num):
        print(x, end=' ')
print('\nFim do programa')
