from ex107 import moeda

p = float(input('Digite o preco: R$'))
print(f'A metade de {p} eh {moeda.metade(p)}')
print(f'O dobro de {p} eh {moeda.dobro(p)} ')
print(f'Aumentando 10%, temos {moeda.aumentar(p, 10)}')
print(f'Reduzindo 13%, temos {moeda.diminuir(p, 13)}')