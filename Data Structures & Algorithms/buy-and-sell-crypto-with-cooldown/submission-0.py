class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {} #key: (i, boolean: buy or not buy) val:maxProfit

        def recursion(i, buyornot):
            if i >= len(prices):
                return 0
            if (i,buyornot) in dp:
                return dp[(i, buyornot)]
            
            cooldown = recursion(i + 1, buyornot)
            if buyornot:
                buy = recursion(i + 1, not buyornot) - prices[i]
                dp[(i, buyornot)] = max(buy, cooldown)
            else:
                sell = recursion(i + 2, not buyornot) + prices[i]
                dp[(i, buyornot)] = max(sell, cooldown)
            
            return dp[(i, buyornot)]
        
        return recursion(0, True)
