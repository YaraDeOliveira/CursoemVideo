print('=='*20)
l1 = float(input('Digite o tamanho em cm de uma reta: '))
l2 = float(input('Digite o tamanho em cm de uma reta: '))
l3 = float(input('Digite o tamanho em cm de uma reta: '))
maiorlado = max(l1, l2, l3)
soma = l1+l2+l3-maiorlado
if soma > maiorlado:
    print('Pode se fazer um triangulo')
else:
    print('Nao da para fazer um triangulo')


# r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2