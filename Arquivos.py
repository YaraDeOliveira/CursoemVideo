#Testando os metodos read(), readline() e readlines()

"""manipulador = open("arquivo1", "r")
print("\nMetodo read(): \n")
print(manipulador.read())

manipulador.seek(0) #Volta para o inicio

print("\nMetodo readline(): \n")
print(manipulador.readline())
print(manipulador.readline())

manipulador.seek(0)

print("\nMetodo readLine(): \n")
print(manipulador.readlines())

manipulador.close()"""

print("Teste de abertura de arquivos em Python")
print("Tentando abrir um arquivo de texto")

manipulador = open("arquivo1", "r")
for linha in manipulador:
    linha = linha.rstrip()
    print(linha)
manipulador.close()
