dados = dict()
gols = list()
dados['nome'] = str(input('Nome do Jogador:'))
part = int(input(f'Quantas partidas {dados["nome"]} jogou?:'))
for c in range(0, part):
    gols.append(int(input(f'Quantos gols na partida {c}?')))
dados['goals'] = gols[:]
dados['total'] = sum(gols)
print(dados)
print("-="*30)
for k, v in dados.items():
    print(f'O campo {k} tem o valor {v}')
print("-="*30)
print(f'O jogador {dados["nome"]} jogou {part} partidas')
for c, q in enumerate(gols):
    print(f'=> Na partida {c}, fez {q} gols.')
print(f'Foi um total de {dados["total"]} goals')
