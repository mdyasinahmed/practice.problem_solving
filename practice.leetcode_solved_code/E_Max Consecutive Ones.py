class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = 0
        summation = 0

        for num in nums:
            if num == 0:
                summation = 0
            else:
                summation += num
                res = max(res, summation)

        return res