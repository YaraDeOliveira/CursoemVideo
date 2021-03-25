def ficha(nome=0, gols=0):
    if not nome:
        nome = '<desconhecido>'
    if not gols:
        gols = 0
    return print(f'O jogador {nome} fez {gols} gol(s) no campeonato.')


print(f'{"FICHA DO JOGADOR":=^35}')
nme = str(input('Nome do Jogador:'))
gol = str(input('Numero de Gols: '))
ficha(nme, gol)
