from datetime import date
ano = int(input('Digite o ano de nascimento: '))
idade = date.today().year - ano
alistar = ano + 18
if idade < 18:
    print('Faltam ainda {} ano(s) para vc se alistar'.format(18-idade))
    print(f'O seu alistamento sera em {alistar}')
elif idade == 18:
    print('Esta na hora de se alistar')
else:
    print('Ja passou {} ano(s) do seu tempo de alistamento'.format(idade-18))
    print('Seu ano de alistamento foi em {}'.format(alistar))
