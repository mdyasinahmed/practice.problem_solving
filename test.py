class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        res = []
        mini = 0
        maxi = len(s)

        for c in s:
            if c == 'I':
                res.append(mini)
                mini += 1
            else:
                res.append(maxi)
                maxi -= 1
        
        return res+[mini]