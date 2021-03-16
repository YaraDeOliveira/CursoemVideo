import emoji
print('==='*15)
print('\033[1;31mSIMULADOR CREDITO IMOBILIARIO')
print('==='*15)
casa = float(input('\033[1mQual o valor do imovel: R$'))
salario = float(input('\033[1mQual o valor do seu salario: R$'))
tempo = int(input('\033[1mQuantos anos deseja financiar: '))
prestacao = casa / (tempo*12)
print('A prestacao sera de R$ {:.2f}'.format(prestacao))
if prestacao <= salario*0.30:
    print(emoji.emojize('\033[1;36;41m Parabens!! Seu emprestimo foi aprovado!! :smile:\033[m', use_aliases=True))
else:
    print('\033[1;36;41m Infelizmente nao vai ser possivel financiar seu imovel\033[m')
