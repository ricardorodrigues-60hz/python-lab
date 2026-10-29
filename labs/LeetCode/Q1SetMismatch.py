from typing import List
"""
You have a set of integers s, which originally contains all the numbers from 1 to n. Unfortunately, due to some error, one of the numbers in s got duplicated to another number in the set, which results in repetition of one number and loss of another number.

You are given an integer array nums representing the data status of this set after the error.

Find the number that occurs twice and the number that is missing and return them in the form of an array.

 

Example 1:

Input: nums = [1,2,2,4]
Output: [2,3]
"""
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