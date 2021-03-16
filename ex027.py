nome = str(input('Digite seu nome completo: ')).strip().title()
div = nome.split()
print('Primeiro nome eh {}'.format(div[0]))
print('Ultimo nome eh {}'.format(div[len(div)-1]))
