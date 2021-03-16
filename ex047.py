print('\033[1;34mNUMEROS PARES DE 1 A 50\033[m')
for c in range(1, 51):
    if c % 2 == 0:
        print(f'{c}', end=' ')
print('FIM')
#or
'''print('\033[1;34mNUMEROS PARES DE 1 A 50\033[m')
for c in range(2, 51, 2):
    print(f'{c}', end=' ')
print('FIM')'''