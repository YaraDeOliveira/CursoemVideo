print('=='*20)
l1 = float(input('Digite o tamanho em cm de uma reta: '))
l2 = float(input('Digite o tamanho em cm de uma reta: '))
l3 = float(input('Digite o tamanho em cm de uma reta: '))
maiorlado = max(l1, l2, l3)
soma = l1+l2+l3-maiorlado
if soma > maiorlado:
    print('Pode se fazer um triangulo')
    if l1 == l2 and l2 == l3 and l1 == l3:
        print('\033[1;32mEQUILATERO\033[m: todos os lados sao iguais')
    elif l1 != l2 and l2 != l3 and l1 != l3:
        print('\033[1;32mESCALENO\033[m: todos os lados sao diferentes')
    else:
        print('\033[1;32mISOSCELES\033[m: dois lados sao iguais')
else:
    print('Nao da para fazer um triangulo')


# r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2