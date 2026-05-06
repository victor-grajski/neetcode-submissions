class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        profit = 0
        maxP = 0
        for r in range(1, len(prices)):
            profit = prices[r] - prices[l]
            maxP = max(maxP, profit)
            if prices[r] < prices[l]:
                l = r
        return maxP
