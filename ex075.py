tabela = (int(input("Digite um numero:")),
       int(input("Digite outro numero:")),
       int(input("Digite mais numero:")),
       int(input("Digite o ultimo numero:")))
par = 0
print(f'Os numeros digitados foram:{tabela}'.replace('(', '').replace(')', ''))
print(f'Foram digitados {tabela.count(9)} vezes o numero 9')
if tabela.count(3) > 0:
    print(f'A primeira vez que apareceu o num 3 foi na posicao {tabela.index(3)+1}')
else:
    print(f'O numero 3 nao foi digitado em nenhuma posicao')
print(f'Os numeros pares sao:', end='')
for c in range(0, len(tabela)):
    if tabela[c] % 2 == 0:
        print(tabela[c], end=' ')