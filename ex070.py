c = soma = baraton = 0
barato = " "
print('-' * 30)
print('\033[1;32mLOJA SUPER BARATAO\033[m')
print('-' * 30)
while True:
    prod = str(input('Nome do Produto:')).capitalize().strip()
    preco = float(input('Preco: R$'))
    if soma == 0 or preco < barato:
        barato = preco
        baraton = prod
    if preco > 1000:
        c += 1
    soma += preco
    avancar = str(input("Quer continuar [S/N]: "))
    while avancar not in 'SsNn':
        avancar = str(input("Quer continuar [S/N]: "))
    if avancar in 'Nn':
        break
print(f"{'Fim do Programa' :=^40}")
print(f'O total da compra foi {soma:.2f}')
print(f'Temos {c} produtos custando mais de R$1000,00')
print(f'O produto mais barato foi {baraton} que custa R${barato:.2f}')

