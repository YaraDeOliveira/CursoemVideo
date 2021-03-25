def notas(*num, sit=False):
    """
    -> Funcao para analisar notas e situacoes dos alunos.
    :param num: uma ou mais notas de um aluno
    :param sit: valor opc, para verificar a situacao em relacao a media.
    :return: dicionario com a ficha do aluno
    """
    ficha = dict()
    ficha['total'] = len(num)
    ficha['maior'] = max(num)
    ficha['menor'] = min(num)
    ficha['media'] = sum(num) / len(num)
    if sit:
        if ficha['media'] >= 7:
            si = "BOA"
        elif 5 < ficha['media'] < 7:
            si = 'RAZOAVEL'
        else:
            si = 'RUIM'
        ficha['Situacao'] = si
    return ficha


resp = notas(3.5, 4, 2, 6.5, 6.4)
print(resp)
help(notas)