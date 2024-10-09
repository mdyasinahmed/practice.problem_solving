class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dupli = set()

        for i, num in enumerate(nums):
            if i>k:
                dupli.remove(nums[i-k-1])
            if num in dupli:
                return True
            dupli.add(num)

        return False