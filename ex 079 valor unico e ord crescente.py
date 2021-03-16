lista = []
while True:
    z = int(input('Digite um valor: '))
    if z in lista:
        print('Valor ja foi digitado')
    else:
        lista.append(z)
        print('Numero adicionado com sucesso')
    cont = str(input('Deseja continuar? [S/N]'))
    while cont not in 'SsNn':
        cont = str(input('Deseja continuar? [S/N]'))
    if cont in 'Nn':
        break
lista.sort()
print(f'Voce digitou os valores {lista}')
