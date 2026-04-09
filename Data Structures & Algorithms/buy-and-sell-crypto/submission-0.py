class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        profit = 0
        maxSum = 0
        while l < len(prices):
            if r >= len(prices):
                l += 1
                r = l + 1
                profit = 0
                continue

            profit = prices[r] - prices[l]
            
            if profit < 0:
                l += 1
                r = l + 1
                profit = 0
            else:
                maxSum = max(maxSum, profit)
                r += 1
        
        return maxSum