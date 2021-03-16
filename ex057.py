sexo = str(input('Informe o seu sexo [M/F]:')).strip().upper()
#while sexo != 'M' and sexo != 'F':
while sexo not in 'MmFf':
    sexo = str(input('Digite o sexo valido[M/F]:')).upper().strip()
print(f'Seu sexo eh {sexo}')
