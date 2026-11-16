from functools import singledispatch

class Amarelo:
    ...

class Verde:
    ...

class Roxo:
    ...


@singledispatch
def jose(evento):
    pass

@jose.register(Roxo)
def mandar_para_centauro(evento):
    print('Centauro recebeu a cor roxa')


@jose.register(Amarelo)
def mandar_para_fausto(evento):
    print('Fausto recebeu a cor Amarelo')


@jose.register(Verde)
def mandar_para_Fada(evento):
    print('Fada recebeu a cor roxa')
