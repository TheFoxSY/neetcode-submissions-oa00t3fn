class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        LIS = [1] * len(nums)
        for i in range(len(nums) - 1, -1, -1):
            for j in range(i - 1, -1, -1):
                if nums[j] < nums[i]:
                    LIS[j] = max(LIS[j], LIS[i] + 1)
        
        return max(LIS)
        