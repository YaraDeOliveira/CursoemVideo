peso = float(input('Digite o seu peso: '))
altura = float(input('Digite sua altura: '))
imc = peso / (altura**2)
print(f'O IMC esta em {imc:.2f}'.format())
if imc < 18.5:
    print('\033[1;33mABAIXO DO PESO')
elif 18.5 < imc < 25:
    print('\033[1;33mPESO IDEAL')
elif 25 <= imc < 30:
    print('\033[1;33mSOBREPESO')
elif 30 <= imc < 40:
    print('\033[1;33mOBESIDADE')
if imc >= 40:
    print('\033[1;33mOBESIDADE MORBIDA')
