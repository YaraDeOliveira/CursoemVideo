dados = dict()
geral = list()
mulher = list()
n = s = m = si = 0
while True:
    dados['nome'] = str(input('Nome:'))
    sexo = str(input('Sexo [F/M]:'))
    while sexo not in 'FfmM':
        sexo = str(input('Sexo [F/M]:'))
    dados['sexo'] = sexo
    if sexo in 'Ff':
        mulher.append(dados['nome'])
    m = int(input('Idade:'))
    dados['idade'] = m
    si += m
    n = n+1
    geral.append(dados.copy())
    cont = str(input('Deseja continuar? [S/N]:'))
    if cont in 'Nn':
        break
print(f'Foram cadastrados {n} pessoas')
media = si / n
print(f'A media de idades foi {media:.2f} anos')
print(f'A lista das mulheres {mulher}')
print(f'Lista das pessoas que estao acima da media de idade',)
for p in geral:
    if p['idade'] >= media:
        print('       ', end='')
        for k, v in p.items():
            print(f'{k} = {v}', end='')
        print()

