n1 = float(input('Digite a nota da primeira avaliacao: '))
n2 = float(input('Digite a nota da segunda avaliacao: '))
media = (n1+n2)/2
if media < 5.0:
    print('\033[1;34mREPROVADO')
elif 5.0 <= media < 7.0:
    print('\033[1;34mRECUPERACAO')
else:
    print('\033[1;34mAPROVADO')