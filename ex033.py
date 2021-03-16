n1 = int(input('Digite o numero 1: '))
n2 = int(input('Digite o numero 2: '))
n3 = int(input('Digite o numero 3: '))
if n1 > n2 and n1 > n3:
    print('O maior numero eh {}'.format(n1))
elif n2 > n1 and n2 > n3:
    print('O maior numero eh {}'.format(n2))
else:
    print('O maior numero eh {}'.format(n3))
if n1 < n2 and n1 < n3:
    print('O menor numero eh {}'.format(n1))
elif n2 < n1 and n2 < n3:
    print('O menor numero eh {}'.format(n2))
else:
    print('O menor numero eh {}'.format(n3))

'''ou
 menor = n1
 if n2<n1 and n2<n3:
    menor = n2
if n3<n1 and n3<n2:
    menor = n3
    
 '''