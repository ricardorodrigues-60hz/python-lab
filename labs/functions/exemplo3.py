"""Des|empacotamento de argumentos."""


def meu_sum(*args):
    """
    definicao generica de parametros
    args* só lida com argumentos explicitamente posicinais
    """
    print(args)
    print(type(args))
    return sum(args)

# def meu_sum2(*grupos_posicional, **grupo_nomeado):
def meu_sum2(*args, **kwargs):
    """
    >>> meu_sum(1,2,3,4,5, a=1, b=2)
    (1,2,3,4,5)      {'a': 1, 'b': 2}
    <class 'tuple'>  <class 'dict'>
    """ 
    print(args, kwargs)
    print(type(args), type(kwargs))
    return args, kwargs


lista = [1, 2, 3, 4]

def meu_min(a, b, c, d):
    """
    >>> meu_min(*lista) #'desempacota' lista
    >>> 1

    Senão seria:
    >>> meu_min(lista[0], lista[1], ...)
    """
    return min((a, b, c, d))
    

dicionario = {
    'a': 1,
    'b': 2,
    'c': 3, 
    'd': 4
}    

def meu_max(a=0, b=0, c=0, d=0):
    """
    >>> meu_max(**dicionario)
    >>> 4
    """
    return max((a, b, c, d))