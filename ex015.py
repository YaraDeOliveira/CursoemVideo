km = int(input('Quantos KM foram percorridos com o carro: '))
dias = int(input('Quantos dias vc alugou o carro?: '))
total = (km*0.15)+(dias*60)
print(f'O total a pagar eh de R${total:.2f}')