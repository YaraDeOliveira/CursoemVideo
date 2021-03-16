from datetime import date
ano = int(input('Digite o ano do seu nascimento: '))
idade = date.today().year - ano
print(f'O atleta tem {idade} anos')
if idade <= 9:
    print('\033[1;34mCLASSIFICACAO: MIRIM')
elif 9 < idade <= 14:
    print('\033[1;34mCLASSIFICACAO: INFANTIL')
elif 14 < idade <= 19:
    print('\033[1;34mCLASSIFICACAO: JUNIOR')
elif 19 < idade <= 20:
    print('\033[1;34mCLASSIFICACAO: SENIOR')
else:
    print('\033[1;34mCLASSIFICACAO: MASTER')
