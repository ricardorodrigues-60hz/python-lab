from typing import List
"""
Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].

Return the array in the form [x1,y1,x2,y2,...,xn,yn].

 

Example 1:

Input: nums = [2,5,1,3,4,7], n = 3
Output: [2,3,5,4,1,7] 
Explanation: Since x1=2, x2=5, x3=1, y1=3, y2=4, y3=7 then the answer is [2,3,5,4,1,7].
"""

def shuffle(nums: List[int], n: int) -> List[int]:
    nums2 = nums[:n]
    nums = nums[n:]
    print(nums2)
    print(nums)
    

    return [item for pair in zip(nums, nums2) for item in pair]

shuffle([1,2,3,4,5,6], 3)

