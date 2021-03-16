n10 = n50 = n20 = n1 = 0
print("="*40)
print(f"{'BANCO CEV':^40}")
print("="*40)
saque = int(input("Valor do saque: R$"))
n50 = saque // 50
if n50 > 0:
    print(f'Total de {n50} cedulas de R$ 50')
n20 = (saque - n50*50) // 20
if n20 > 0:
    print(f'Total de {n20} cedulas de R$ 20')
n10 = (saque - n50*50 - n20*20) // 10
if n10 > 0:
    print(f'Total de {n10} cedulas de R$ 10')
n1 = (saque - n50*50 - n20*20 - n10*10) // 1
if n1 > 0:
    print(f'Total de {n1} cedulas de R$ 1')
print('='*40)
print('Tenha um bom dia')
