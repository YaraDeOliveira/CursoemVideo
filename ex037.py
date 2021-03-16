num = int(input('Digite um numero qualquer: '))
opcao = int(input('Qual conversao vc deseja fazer:\n'
                  '1 - BINARIO\n'
                  '2 - OCTAL\n'
                  '3 - HEXADECIMAL\n'
                  'Sua opcao: '))
if opcao == 1:
    print('O numero {} em BINARIO eh {}'.format(num, bin(num)[2:]))
elif opcao == 2:
    print('O numero {} em OCTAL eh {}'.format(num, oct(num)[2:]))
elif opcao == 3:
    print('O numero {} em HEXADECIMAL eh {}'.format(num, hex(num)[2:]))
else:
    print('Opcao invalida')
