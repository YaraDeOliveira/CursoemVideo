n = int(input("Digite qtos elementos da\nSequencia de Fibonacci deseja ver: "))
c = 0
x = 0
aux = 1
aux2 = 0
while x != (n-1):
    print(c, end='->')
    aux2 = c
    c = aux + aux2
    aux = aux2
    x = x + 1
print(c)