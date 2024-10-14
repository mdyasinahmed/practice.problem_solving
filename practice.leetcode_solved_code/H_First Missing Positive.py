class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        size = len(nums)

        for i in range(size):
            while nums[i] > 0 and nums[i] <= size and nums[nums[i] - 1] != nums[i]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
            
        for i, num in enumerate(nums):
            if num != i+1:
                return i+1

        return size+1