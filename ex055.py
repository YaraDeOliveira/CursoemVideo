maior = 0
menor = 0
for c in range(0, 5):
    peso = float(input(f'{c+1}:Digite o peso: '))
    if c == 0:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

    '''if peso > maior:
        maior = peso
        if menor == 0:
            menor = peso
    elif peso < menor:
            menor = peso'''
print(f'O maior peso foi {maior} e o menor peso foi {menor}')

