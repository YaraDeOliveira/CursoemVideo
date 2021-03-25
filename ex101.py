def voto(ano):
    from datetime import date
    idade = date.today().year - ano
    print(f'Com {idade} anos: ', end='')
    if idade < 16:
        return print('Voto Negado')
    elif 16 < idade < 18 or idade > 65:
        return print('Voto Opcional')
    else:
        return print('Voto Obrigatorio')


print(f'{"Eleicao":=^30}')
anos = int(input('Digite o ano do seu nascimento: '))
voto(anos)
