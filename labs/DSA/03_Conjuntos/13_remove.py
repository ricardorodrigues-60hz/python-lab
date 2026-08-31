numeros = {1, 2, 3, 1, 2, 1, 4, 5, 6, 7, 8, 8, 8, 9, 10}

numeros # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
numeros.remove(5) # {1, 2, 3, 4, 6, 7, 8, 9, 10}
numeros.remove(11) # KeyError: 11
