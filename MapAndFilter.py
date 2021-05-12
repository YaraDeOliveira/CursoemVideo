#numeros = [1, 2, 3, 4, 5]
#output = list(map(lambda var: var**2, numeros))
#print(output)

numeros = [1, 2, 3, 4, 5]
output = list(filter(lambda x: x >= 3, numeros))
print(output)