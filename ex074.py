from random import randint
n = (randint(0, 10), randint(0, 10), randint(0, 10),
     randint(0, 10), randint(0, 10))
print(f'Os numeros sorteados foram {n}'.replace("(", '', ).replace(')', ''))
print(f'O maior numero sorteado foi {max(n)}')
print(f'O menor numero sorteado foi {min(n)}')
