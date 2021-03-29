def leiaInt(msg):
    while True:
        try:
            z = int(input(msg))
        except KeyboardInterrupt:
            print('\n\033[32mUsuario preferiu nao digitar esse numero\033[m')
            return 0
        except:
            print('\033[32mERRO! Digite um numero inteiro\033[m')
        else:
            return z


def leiaReal(msg):
    while True:
        try:
            c = float(input(msg))
        except KeyboardInterrupt:
            print('\n\033[32mUsuario preferiu nao digitar esse numero\033[m')
            return 0
        except:
            print('\033[32mERRO! Digite um numero real\033[m')
        else:
            return c


n = leiaInt('Digite um numero inteiro: ')
x = leiaReal('Digite um numero Real: ')
print(f'O valor inteiro digitado foi {n} e o real {x}')






