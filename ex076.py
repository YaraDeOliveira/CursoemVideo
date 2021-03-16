listagem = 'LAPIS', '1,75', 'BORRACHA', '2,00', 'CADERNO', '15,90', 'ESTOJO', '25,00', 'TRANSFERIDOR', '4,20', 'COMPASSO', '9,99', 'MOCHILA', '120,32', 'CANETAS', '22,30', 'LIVRO', '34,90'
print('_'*40)
print(f'{"LISTAGEM DE PRECOS":^40}')
print('-'*40)
for c in range(0, len(listagem), 2):
    print(f'{listagem[c]:.<30} R${listagem[c+1]:>8}')
print('-'*40)

