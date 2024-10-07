class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        x = 0
        y = -math.inf

        for price in prices:
            x = max(x, y+price)
            y = max(y, -price)

        return x