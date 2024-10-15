class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        summation = sum(nums)
        prefix = 0

        for i, num in enumerate(nums):
            if prefix == summation - prefix - num:
                return i
            prefix += num
    
        return -1