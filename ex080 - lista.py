lista = list()
c = 0
for c in range(0, 5):
    z = int(input('Digite um valor:'))
    if c == 0:
        lista.append(z)
        print('Valor adicionado ao final da lista')
    else:
        if z < min(lista):
            lista.insert(0, z)
            print(f'Valor adicionado na posicao {lista.index(z)} da lista ')
        elif z > max(lista):
            lista.append(z)
            print('Numero adicionado no final da lista')
        elif min(lista) < z < max(lista):
            if min(lista) < z < lista[1]:
                lista.insert(1, z)
                print(f'Valor adicionado na posicao {lista.index(z)} da lista ')
            elif lista[1] < z < lista[2]:
                lista.insert(2, z)
                print(f'Valor adicionado na posicao {lista.index(z)} da lista ')
            else:
                lista.insert(3, z)
                print(f'Valor adicionado na posicao {lista.index(z)} da lista ')
        if c > 3:
            if lista[1] > lista[2]:
                c = lista[1]
                lista[1] = lista[2]
                lista[2] = c
            elif lista[2] > lista[3]:
                c = lista[2]
                lista[2] = lista[3]
                lista[3] = c
print(lista)
