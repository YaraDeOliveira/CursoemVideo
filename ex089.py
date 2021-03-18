from time import sleep
geral = [[], [], []]
media = 0
nota = list()
while True:
    nome = str(input('Nome:'))
    nota.append(float(input('Nota 1:')))
    nota.append(float(input('Nota 2:')))
    media = (nota[0]+nota[1]) / 2
    geral[2].append(media)
    geral[0].append(nome)
    geral[1].append(nota[:])
    nota.clear()
    media = 0
    cont = str(input('Quer continuar?[S/N]'))
    while cont not in 'SsNn':
        cont = str(input('Quer continuar?[S/N]'))
    if cont in 'Nn':
        break
print('-='*20)
print('No.   NOME           MEDIA')
print('-='*20)
for c in range(0, len(geral[0])):
    print(f'{c}     {geral[0][c]:<15}  {geral[2][c]:>5.1f}')
while True:
    cont2 = int(input('Mostrar notas de qual aluno? (pare = 999)'))
    if cont2 == 999:
        break
    while cont2 > len(geral[0]):
        cont2 = int(input('Mostrar notas de qual aluno? (pare = 999)'))
    print(f' As notas de {geral[0][cont2]} foram {geral[1][cont2]}')
    print('-='*20)
print('Finalizando...')
sleep(0.5)
print(f'{"VOLTE SEMPRE":^20}')