num = []
for c in range(0, 5):
    num.append(int(input(f'Digite um numero para posicao {c}:')))
print(f'Os numeros digitados foram: {num}')
print(f'O maior numero digitado foi: {max(num)}, na posicao {num.index(max(num))} ')
print(f'O menor numero digitado foi: {min(num)}, na posisao {num.index(min(num))}')
