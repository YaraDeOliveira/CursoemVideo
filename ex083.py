expressao = str(input('Digite a expressao:'))
pilha = []
for s in expressao:
    if s == '(':
        pilha.append('(')
    elif s == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressao esta correta')
else:
    print('Sua expressao esta incorreta')
print(pilha)