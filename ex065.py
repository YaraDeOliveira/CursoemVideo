n = 'S'
x = soma = maior = menor = z = 0
while n in 'Ss':
    x = int(input('Digite um numero:'))
    soma += x
    z += 1
    if z == 1:
        menor = maior = x
    if x > maior:
        maior = x
    if x < menor:
        menor = x
    n = str(input('Quer continuar [S/N]')).upper().strip()
print('Foram digitados {} numeros'
      '\na media entre eles eh {:.2f}'
      '\no maior numero eh {}'
      '\no menor numero eh {}'.format(z, soma/z, maior, menor))


