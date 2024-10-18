class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        res = 0
        initHeight = 1
        count = [0]*101

        for height in heights:
            count[height] += 1
        
        for height in heights:
            while count[initHeight] == 0:
                initHeight+=1
            
            if height != initHeight:
                res += 1
            count[initHeight] -= 1
        
        return res