conjunto_a = {1, 2, 3}
conjunto_b = {4, 1, 2, 5, 6, 3}

conjunto_a.issuperset(conjunto_b) # False
conjunto_b.issuperset(conjunto_a) # True
print(conjunto_a.issuperset(conjunto_b))
print(conjunto_b.issuperset(conjunto_a))