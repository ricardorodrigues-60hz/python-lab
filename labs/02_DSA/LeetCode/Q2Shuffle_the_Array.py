from typing import List


def shuffle(nums: List[int], n: int) -> List[int]:
    nums2 = nums[:n]
    nums = nums[n:]
    print(nums2)
    print(nums)
    

    return [item for pair in zip(nums, nums2) for item in pair]

shuffle([1,2,3,4,5,6], 3)

