class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dp = [False] * len(nums)
        dp[0] = True

        for i in range(len(nums)):
            if dp[i] and i + nums[i] >= len(nums):
                return True
            if dp[i]:
                for j in range(1, nums[i] + 1):
                    dp[i + j] = True
        
        return dp[len(nums) - 1]
            
            
        