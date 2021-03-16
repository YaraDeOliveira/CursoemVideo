lista = []
z = 0
while True:
    lista.append(int(input('Digite um valor:')))
    z += 1
    cont = str(input('Deseja continuar:[S/N]'))
    while cont not in 'SsNn':
        cont = str(input('Deseja continuar:[S/N]'))
    if cont in 'Nn':
        break
print(f'Foram digitados {z} valores: {lista} ')
lista.sort()
print(f'Os numeros em ordem crescente: {lista}')
lista.sort(reverse=True)
print(f'Os numeros em ordem decrescente sao: {lista}')
if 5 in lista:
    print(f'O numero 5 esta na lista, posicao {lista.index(5)} da lista em ordem decrescente')
else:
    print('O numero 5 nao esta na lista')
