"""
Argumentos posicionais, nomeados.
"""


anonima = lambda param: param + 2
anonima_plus = lambda param1, param2: param1  +  param2


def soma_posicional(x, y):
    """X e Y são parametros posicionais."""
    return x + y


def soma_nomeados(x=7, y=7):
    """
    X e Y são parametros nomeados.
    
    Na Falta de X ou Y, o valor 7 será usado. 
    """
    print(f'x: {x}, y: {y}')
    return x + y


def soma_excplicitamente_nomeados(*, x=7, y=7):
    """
    X e Y são parametros nomeados.
    
    Na Falta de X ou Y, o valor 7 será usado. 
    """
    print(f'x: {x}, y: {y}')
    return x + y


def soma_excplicitamente_nomeados2(x=7, *, y=7):
    """
    X e Y são parametros nomeados.
    
    Na Falta de X ou Y, o valor 7 será usado. 
    """
    print(f'x: {x}, y: {y}')
    return x + y


def soma_excplicitamente_posicional(x, y, /):
    """
    X e Y são parametros nomeados.
    
    Na Falta de X ou Y, o valor 7 será usado. 
    """
    print(f'x: {x}, y: {y}')
    return x + y


def suma_tudo_mix(x, y, /, z, *, w):
    return sum((x, y, z, w))