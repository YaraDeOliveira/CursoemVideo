sal = float(input('Digite o salario: R$'))
if sal < 1250.00:
    novo = sal+(sal*0.15)
    print('Vc ganhou um aumento de 15%. O seu novo salario sera de: R${}'.format(novo))
else:
    novo = sal+(sal*0.10)
    print('Vc ganhou um aumento de 10%. O seu novo salario sera de: R${}'.format(novo))
