while True:
    print(f'\033[1;30;43m{"~"*40}')
    print(f'{"SISTEMA DE AJUDA PyHELP":^40}')
    print(f'{"~"*40}')
    print(f'\033[m')
    x = str(input("Funcao ou Biblioteca:")).lower().strip()
    if x == 'fim':
        break
    print(f'\033[1;30;44m{"~" * 40}')
    print(f'  Acessando o manual do comando {x}')
    print(f'{"~" * 40}')
    print(f'\033[42m')
    help(x)