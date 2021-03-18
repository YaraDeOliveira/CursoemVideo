from time import sleep
ficha = list()
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1:'))
    nota2 = float(input('Nota 2:'))
    media = (nota1+nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    resp = str(input('Quer continuar? [S/N]'))
    if resp in 'Nn':
        break
print('-='*30)
print(f'{"No.":<4}{"NOME":<10}{"MEDIA":>8}')
print('-'*30)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:8.1f}')
while True:
    cont2 = int(input('Mostrar notas de qual aluno? (pare = 999)'))
    if cont2 == 999:
        break
    if cont2 <= len(ficha):
        print(f'Notas de {ficha[cont2][0]} sao {ficha[cont2][1]}')
print('Finalizando...')
sleep(0.5)
print(f'{"VOLTE SEMPRE":^20}')