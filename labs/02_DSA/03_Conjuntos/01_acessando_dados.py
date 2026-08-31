numeros = {1, 2, 3, 4, 5, 1, 2, 3, 4, 5}
# print(numeros[0]) # TypeError: 'set' object is not subscriptable

numeros = list(numeros)
print(numeros[0]) # 1