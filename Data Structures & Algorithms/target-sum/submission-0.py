class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        def dfs(i, amount):
            if i == len(nums) and amount == target:
                return 1
            if i >= len(nums):
                return 0
            

            result1 = dfs(i + 1, amount - nums[i])
            result2 = dfs(i + 1, amount + nums[i])

            return result1 + result2

        return dfs(0, 0)

        