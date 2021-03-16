vel = float(input('Qual eh a velocidade do carro? '))
if vel > 80:
    multa = float(vel-80)*7.00
    print('Voce foi multado em R${:.2f}'.format(multa))
else:
    print('Voce nao foi multado. Tenha um bom dia!')
