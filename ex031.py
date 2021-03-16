distance = float(input('Qual eh a distancia da viagem: '))
if distance < 200:
    preco = distance*0.50
    print('O preco da passagem eh de R${:.2f}'.format(preco))
else:
    preco = distance*0.45
    print('O preco da passagem eh de R${:.2f}'.format(preco))
