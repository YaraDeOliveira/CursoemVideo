'''Exercício Python 22: Crie um programa que leia
o nome completo de uma pessoa e mostre:
– O nome com todas as letras maiúsculas e minúsculas.
– Quantas letras ao todo (sem considerar espaços).
– Quantas letras tem o primeiro nome.'''


nome = str(input('Digite o seu nome completo: ')).strip()
print('Seu nome em letras maiusculas eh {}'.format(nome.upper()))
print('Seu nome em letras minusculas eh {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'. format(len(nome)-nome.count(' ')))
dividido = nome.split()
print('Seu primeiro nome tem {} letras'.format(len(dividido[0])))
#print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))