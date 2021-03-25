def leiaInt(num):
    x = input(num)
    if x.isnumeric():
        return x
    else:
        while True:
            print(f"\033[31mERRO! Digite um numero inteiro valido.\033[m")
            x = input(num)
            if x.isnumeric():
                return x


print('-'*34)
n = leiaInt('Digite um numero: ')
print(f'Voce acabou de digitar o numero {n}')