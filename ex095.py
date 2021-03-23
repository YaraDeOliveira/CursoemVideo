dados = dict()
gols = list()
geral = list()
while True:
    dados['nome'] = str(input('Nome do Jogador:'))
    part = int(input(f'Quantas partidas {dados["nome"]} jogou?:'))
    for c in range(0, part):
        gols.append(int(input(f'Quantos gols na partida {c+1}?')))
    dados['goals'] = gols.copy()
    dados['total'] = sum(gols)
    gols.clear()
    geral.append(dados.copy())
    cont = str(input('Deseja continuar? [S/N]'))
    while cont not in 'NnSs':
        cont = str(input('Deseja continuar? [S/N]'))
    if cont in 'Nn':
        break
    print("-=" * 30)
print("-="*30)
print('cod ', end='')
for i in dados.keys():
    print(f'{i:<15}', end='')
print()
for k, v in enumerate(geral):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print("-="*30)
while True:
    busca = int(input('Mostar dados de qual jogador? [999 para parar]:'))
    if busca == 999:
        break
    if busca >= len(geral):
        print(f'Nao existe jogador para esse codigo {busca}')
    else:
        print(f' -- Levantamento do Jogador {geral[busca]["nome"]}:')
        for i, g in enumerate(geral[busca]["goals"]):
            print(f'No jogo {i+1} fez {g} gols       ')
    print("-="*30)
print('fim')
