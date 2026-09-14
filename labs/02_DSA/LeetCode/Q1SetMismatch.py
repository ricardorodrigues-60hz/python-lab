from typing import List

def findErrorNums(nums: List[int]) -> List[int]:
    n = len(nums)
    soma_ideal = n * (n + 1) // 2
    soma_real = sum(nums)
    soma_unicos = sum(set(nums))
    duplicado = soma_real - soma_unicos
    faltante = soma_ideal - soma_unicos
    
    return [duplicado, faltante]

#   return [((sum(nums)) - (sum(set(nums)))), ((len(nums) * (len(nums)+1) // 2) - (sum(set(nums))))]

print(findErrorNums([1, 2, 2, 4]))