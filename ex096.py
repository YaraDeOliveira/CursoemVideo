def area(d, f):
    tot = d * f
    print(f'A area de um terreno {d} x {f} eh de {tot}m²')


print(f'{"CONTROLE DE TERRENOS":^30}')
print('-'*35)
a = float(input('LARGURA (m): '))
b = float(input('COMPRIMENTO (m): '))
area(a, b)
