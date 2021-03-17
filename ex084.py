galera = list()
dados = list()
leve = list()
pesado = list()
menor = maior = 0
while True:
    dados.append(str(input('Nome: ')))
    peso = float(input('Peso: '))
    dados.append(peso)
    if menor == 0 or peso < menor:
        menor = peso
    elif peso > maior:
        maior = peso
    galera.append(dados[:])
    dados.clear()
    cont = str(input('Deseja continuar? [S/N]'))
    while cont not in 'SsNn':
        cont = str(input('Deseja continuar? [S/N]'))
    if cont in 'Nn':
        break
for p in galera:
    if p[1] == menor:
        leve.append(p[0])
    elif p[1] == maior:
        pesado.append(p[0])
print(f'Voce cadastrou {len(galera)} pessoas')
print(f'O maior peso foi de {maior}Kg. Peso de {pesado}')
print(f'O menor peso foi de {menor}Kg. Peso de {leve} ')
