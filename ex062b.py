print('Gerador de PA')
print('-='*10)
primeiro = int(input('Digite o primeiro termo:'))
razao = int(input('Digite a razao da PA'))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print(termo, '- ', end='')
        termo += razao
        cont += 1
    print('Pausa')
    mais = int(input('Qtdos termos vc quer a mais:'))
print('Progressao Finalizada com {} termos'.format(cont))