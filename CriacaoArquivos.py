#Criando e escrevendo em arquivos de texto (modo 'w')

'''arquivo = open("arq01", "w")
arquivo.write("Boson Treinamentos\n")
arquivo.write("Criando um arquivo de texto com Python\n")
arquivo.write("Arquivo criado por Yara de Oliveira\n")
arquivo.write("Esta dando tudo certo\n")
arquivo.close()

#Lendo o arquivo criado
arquivo = open("arq01", "r")
for linha in arquivo:
    linha = linha.rstrip()
    print(linha)
arquivo.close()'''

#Acrescentando textos ao arquivo criado usando o modo "a"
'''print("\n")
texto = input("Digite a frase para acrescentar no arquivo: ")
arquivo = open("arq01", "a")
arquivo.write(texto + "\n")
print("Operacao efetuada com sucesso!!" + arquivo.name + " usando o modo de acesso " + arquivo.mode)
arquivo.close()

print("\nTexto Alterado:")
arquivo = open("arq01", "r")
for linha in arquivo:
    linha = linha.rstrip()
    print(linha)
arquivo.close()'''
