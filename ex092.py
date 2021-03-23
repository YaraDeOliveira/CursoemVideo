import datetime
dados = dict()
dados['nome'] = str(input('Nome:'))
ano = int(input('Ano de Nascimento:'))
idade = datetime.date.today().year - ano
dados['idade'] = idade
ctps = int(input('Carteira de trabalho (0 nao tem):'))
if ctps == 0:
    dados['ctps'] = 0
else:
    dados['ctps'] = ctps
    dados['contratacao'] = int(input('Ano de contratacao:'))
    dados['salario'] = float(input('Salario: R$'))
    dados['aposentadoria'] = (dados['contratacao']+35)-ano
for k, v in dados.items():
    print(f'{k} tem valor {v}')