def fatorial(n, show=False):
    """
    -> Calcula o fatorial de um numero.
    :param n: O numero a ser calculado.
    :param show: (opc) Mostra ou nao a conta.
    :return: O valor do fatorial de n.
    """
    fat = 1
    c = n
    while c > 0:
        fat *= c
        if show:
            while c > 1:
                print(f'{c} x ', end='')
                c -= 1
            if c == 1:
                print(f'{c} = ', end='')
                c -= 1
        else:
            c -= 1
    return fat


print((fatorial(6, True)))
