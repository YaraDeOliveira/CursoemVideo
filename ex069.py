maior = 0
homem = 0
mulhermenor = 0
pes = 0
while True:
    print('-'*40)
    print('CADASTRE UMA PESSOA')
    print('-' * 40)
    idade = int(input('Digite sua idade:'))
    pes += 1
    if idade > 18:
        maior += 1
    sexo = str(input('Digite o seu sexo:[M/F]'))
    while sexo not in 'MmFf':
        sexo = str(input('Digite o sexo valido:[M/F]'))
    if sexo in 'Mm':
        homem += 1
    elif sexo in 'Ff' and idade < 20:
        mulhermenor += 1
    cont = str(input('Deseja continuar? [S/N]'))
    while cont not in 'SsNn':
        cont = str(input('Deseja continuar? [S/N]'))
    if cont in 'Nn':
        break
print(f'Foram {pes} pessoas cadastradas\n'
      f'Foram {maior} pessoas maiores de 18 anos\n'
      f'Foram {homem} homem cadastrados\n'
      f'Foram {mulhermenor} mulheres com menos de 20 anos.\n'
      f'FIM DO PROGRAMA')
