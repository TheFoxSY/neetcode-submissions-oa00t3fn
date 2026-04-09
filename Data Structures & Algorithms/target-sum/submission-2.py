class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = defaultdict(int)

        dp[0] = 1 # 1 way to sum up to 0 with first 0 elements

        for i in range(len(nums)):
            nextDp = defaultdict(int)
            for cur_sum, count in dp.items():
                nextDp[cur_sum + nums[i]] += count
                nextDp[cur_sum - nums[i]] += count
            dp = nextDp
        
        return dp[target]

        