n = int(input("Digite um numero inteiro.\nPara sair digite 999:"))
x = 0
soma = 0
while n != 999:
    soma += n
    x += 1
    n = int(input("Digite um numero inteiro.\nPara sair digite 999:"))
print(f"A soma foi de {soma} e a qtde de numeros foram {x}")