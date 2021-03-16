n = str(input('Digite uma frase:')).lower().strip().replace(' ', '')
y = len(n)
x = len(n)//2
s = 0
inverso = n[::-1]
print(n, inverso)
for c in range(0, x+1):
    if n[c] == n[y-1]:
        s = s+1
        y = y-1
if s == x+1:
    print('E um palindromo')
else:
    print('Nao eh um palindrono')
