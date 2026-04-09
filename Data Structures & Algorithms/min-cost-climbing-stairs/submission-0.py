class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0] * (len(cost) + 1)

        for i in range(2, len(cost)):
            dp[i] = min(dp[i - 2] + cost[i - 2], dp[i - 1] + cost[i - 1])
        
        dp[-1] = min(dp[len(cost) - 1] + cost[len(cost) - 1], dp[len(cost) - 2] + cost[len(cost) - 2])

        return dp[-1]