import math
ang = float(input('Digite o angulo: '))
seno = math.sin(math.radians(ang))
cosseno = math.cos(math.radians(ang))
tangente = math.tan(math.radians(ang))
print('Para o angulo de {} temos:\nseno = {:.2f} \ncosseno = {:.2f}\nTangente = {:.2f}'.format(ang, seno, cosseno, tangente))

