geral = []
par = []
impar = []
while True:
    geral.append(int(input('Digite um numero:')))
    cont = str(input('Deseja continuar [S/N]:'))
    while cont not in 'SsNn':
        cont = str(input('Deseja continuar:[S/N]'))
    if cont in 'Nn':
        break
for z in geral:
    if z % 2 == 0:
        par.append(z)
    else:
        impar.append(z)
print(f'Os numeros digitados foram: {geral} ')
print(f'os numeros pares foram: {par}')
print(f'Os numeros impares foram: {impar}')

