from random import randint
from time import sleep
num1 = randint(0, 5)
print('Vou pensar em um numero... TENTE ADIVINHAR!!')
print('-=-' * 20)
num2 = int(input('Digite um numero de 0 a 5: '))
print('-=-' * 20)
print('Processando...')
sleep(2)
if num2 < 0 or num2 > 5:
    print('Numero Invalido')
elif num1 == num2:
    print('PARABENS VC CONSEGUIU ME VENCER!!')
else:
    print('Que pena! O numero q pensei foi {} e vc pensou em {}'.format(num1,num2))






