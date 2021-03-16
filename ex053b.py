frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]
#inverso = ''
#for letra in range(len(junto)-1, -1, -1):
#    inverso += junto[letra]
print(junto, inverso)
if inverso == junto:
    print(f'{frase} eh um palindromo')
else:
    print(f'{frase} Nao eh um palindromo')