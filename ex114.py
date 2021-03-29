import urllib.request

try:
    url = urllib.request.urlopen('http://www.pudim.com.br/')
except urllib.request.URLError:
    print('Nao foi possivel acessar o site pudim')
else:
    print('Consegui abrir o site pudim com sucesso')