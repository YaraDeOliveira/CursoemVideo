#Desenvolva um programa que leia o nome, idade e sexo
# de 4 pessoas.No final do programa, mostre:
# a média de idade do grupo,
# qual é o nome do homem mais velho e
# quantas mulheres têm menos de 20 anos.

soma = 0
maioridade = 0
nomevelho = ''
contm = 0
for c in range(1, 5):
    print(f'----- {c} PESSOA -----')
    nome = str(input('Digite o seu nome:')).strip()
    idade = int(input('Digite sua idade:'))
    soma += idade
    sexo = str(input('Sexo [M/F]')).strip().upper()
    if sexo == 'M'and maioridade == 0:
        nomevelho = nome
    if sexo == 'M' and idade > maioridade:
        nomevelho = nome
        maioridade = idade
    if sexo == 'F' and idade < 20:
        contm += 1
print('A media de idades eh:{}'.format(soma/4))
print(f'O homem mais velho eh {nomevelho} com {maioridade} anos')
print(f'Sao {contm} mulheres menores que 20 anos')