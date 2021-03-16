from datetime import date
m = 0
x = 0
for c in range(0, 7):
    ano = int(input(f'{c+1}:Digite o ano do seu nascimento: '))
    idade = date.today().year-ano
    if idade > 20:
        m += 1
    else:
        x += 1
print(f'Sao {m} pessoas maiores de idade e {x} menor de idade')

