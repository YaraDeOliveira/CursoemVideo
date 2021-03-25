def notas(*num, sit=False):
    """
    -> Funcao para analisar notas e situacoes dos alunos.
    :param num: uma ou mais notas de um aluno
    :param sit: valor opc, para verificar a situacao em relacao a media.
    :return: dicionario com a ficha do aluno
    """
    s = m = l = a = 0
    for c, d in enumerate(num):
        s += d
        if c == 0:
            m = l = d
        if d > m:
            m = d
        if d < l:
            l = d
    a = s / len(num)
    ficha = {'total': len(num), 'maior': m, 'menor': l, 'media': a}
    if sit:
        if a >= 7:
            si = "BOA"
        elif 5 < a < 7:
            si = 'RAZOAVEL'
        else:
            si = 'RUIM'
        ficha['Situacao'] = si
    return ficha


resp = notas(3.5, 4, 2, 6.5, 6.4, sit=True)
print(resp)