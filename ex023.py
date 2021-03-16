'''Faça um programa que leia um número de
0 a 9999 e mostre na tela cada um dos
dígitos separados.'''

'''num = input('Digite um numero de 0 a 9999: ')
num = num.zfill(4)
print('unidade:', num[3])
print('dezena: ', num[2])
print('centena:', num[1])
print('milhar:', num[0])'''

num1 = int(input('Digite um numero de 0 a 9999 '))
u = num1 // 1 % 10
d = num1 // 10 % 10
c = num1 // 100 % 10
m = num1 // 1000 % 10

print('Analisando o numero {}'.format(num1))
print('unidade: {}'.format(u))
print('dezena: {}'.format(d))
print('centena: {}'.format(c))
print('milhar: {}'.format(m))