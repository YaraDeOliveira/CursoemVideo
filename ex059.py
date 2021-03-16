print('\033[1;32m{:=^40}\033[m'.format('CALCULADORA'))
n1 = int(input('Digite um numero:'))
n2 = int(input('Digite outro numero: '))
opcao = 0
while opcao != 5:
    print('\033[1;34m{:=^30}\033[m'.format('MENU'))
    print('Qual operacao voce deseja efetuar:')
    opcao = int(input('(1) Somar\t(4) Novos numeros\n'
                      '(2) Multiplicar\t (5) Sair do Programa\n'
                      '(3) Maior\n'
                      '\033[1;36mOPCAO: \033[m'))
    if opcao == 1:
        total = n1 + n2
        print(f'A soma entre {n1} e {n2} eh {total}')
    elif opcao == 2:
        total = n1 * n2
        print(f'O produto entre {n1} e {n2} sera de {total}')
    elif opcao == 3:
         print('O maior numero entre {} e {} eh {}'.format(n1, n2, max(n1, n2)))
    elif opcao == 4:
        print('Digite os novos numeros:')
        n1 = int(input('Digite um numero:'))
        n2 = int(input('Digite outro numero: '))
    else:
        print('Digite uma opcao valida!')
print('\33[1;32m{:=^40}\033[m'.format('FIM DO PROGRAMA'))


