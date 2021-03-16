print('\033[1;32m{:=^40}\033[m'.format('LOJAS YARA'))
vbruto = float(input('Qual o valor total bruto: '))
pgto = int(input('Digite a forma de pagamento:\n'
                 '1 - A VISTA (DINHEIRO/CHEQUE\n'
                 '2 - A VISTA (CARTAO)\n'
                 '3 - 2X NO CARTAO\n'
                 '4 - 3X OU MAIS NO CARTAO\n'
                 '\033[1;32mOPCAO: '))
if pgto == 1:
    total = vbruto - (vbruto * 0.10)
    print('O valor total a ser pago e R${:.2f}'.format(total))
elif pgto == 2:
    total = vbruto - (vbruto * 0.05)
    print('O valor total a ser pago e R${:.2f}'.format(total))
elif pgto == 3:
    print('O valor total a ser pago e R${}'.format(vbruto))
elif pgto == 4:
    qtde = int(input('Quantas parcelas? '))
    if qtde <= 2:
        print('Essa opcao eh somente para tres parcelas ou mais')
    else:
        total = vbruto + vbruto * 0.20
        parcela = total / qtde
        print('Sua compra sera parcelada em {}x de R${} COM JUROS'.format(qtde, parcela))
        print('O valor total a ser pago e {}'.format(total))
else:
    print('Opcao Invalida')
