soma = 0
maioridade = 0
nomevelho = ''
contm = 0
for c in range(1, 5):
    print(f'----- {c} PESSOA -----')
    nome = str(input('Digite o seu nome:')).strip()
    idade = int(input('Digite sua idade:'))
    soma += idade
    sexo = str(input('Sexo [M/F]')).strip()
    if sexo in 'Mm' and idade > maioridade:
        nomevelho = nome
        maioridade = idade
    if sexo in 'Ff' and idade < 20:
        contm += 1
print('A media de idades eh:{}'.format(soma/4))
print(f'O homem mais velho eh {nomevelho} com {maioridade} anos')
print(f'Sao {contm} mulheres menores que 20 anos')