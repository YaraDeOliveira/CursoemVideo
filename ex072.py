extenso = ('zero', 'um', 'dois', 'tres', 'quatro',
           'cinco', 'seis', 'sete', 'oito',
           'nove', 'dez', 'onze', 'doze',
           'treze', 'quatorze', 'quinze', 'dezesseis',
           'dezesete', 'dezoito', 'dezenove', 'vinte')
while True:
    num = int(input('Digite um numero entre 0 e 20:')).__ceil__()
    while (num < 0) or (num > 20):
        num = int(input('Por gentileza, digite um numero entre 0 e 20:'))
    print(f'Voce digitou o numero {extenso[num]}')
    cont = str(input('Deseja continuar?[S/N]'))
    while cont not in 'SsNn':
        cont = str(input('Deseja continuar?[S/N]'))
    if cont in 'Nn':
        break
print('Fim do Programa')
