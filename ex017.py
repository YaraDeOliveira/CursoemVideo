from math import hypot
'''catop = float(input('Digite o comprimento do cateto oposto: '))
catad = float(input('Digite o comprimento do cateto adjacente: '))
# hipot2 = (pow(catop, 2)) + (pow(catad, 2))
# hipot = math.sqrt(hipot2)
# ou
hipot = (catop**2+catad**2)**(1/2)

print(f'O valor da hipotenusa eh: {hipot:.2}')'''

catop = float(input('Digite o comprimento do cateto oposto: '))
catad = float(input('Digite o comprimento do cateto adjacente: '))
hi = hypot(catop, catad)
print(f'O valor da hipotenusa eh: {hi:.2f}')

