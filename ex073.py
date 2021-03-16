tabela = ('FLAMENGO', 'INTERNACIONAL', 'ATLÉTICO-MG ',
          'SÃO PAULO', 'FLUMINENSE', 'GRÊMIO',
          'PALMEIRAS', 'SANTOS', 'ATLETICO-PR', 'BRAGANTINO',
          'CEARÁ', 'CORINTHIANS', 'ATLÉTICO-GO',
          'BAHIA', 'SPORT', 'FORTALEZA', 'VASCO',
          'GOIÁS', 'CORITIBA', 'BOTAFOGO')
print(f'Lista de times do Brasileirao: {tabela}')
print('-=-'*30)
print(f'Os primeiro cinco colocados sao:\n{tabela[:5]}')
print('-=-'*30)
print(f'Os quatro ultimos colocados foram:\n{tabela[-4:]}')
print('-=-'*30)
print(sorted(tabela))
print('-=-'*30)
print(f'O Bragantino esta na {tabela.index("BRAGANTINO")+1} colocacao')
print(f'O time campeao foi {tabela[0]}')
