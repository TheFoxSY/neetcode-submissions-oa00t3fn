class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 == 1:
            return False
        target = sum(nums) // 2
        dp = set()
        dp.add(0)
        
        for i in range(len(nums)):
            nextDP = set()
            for j in dp:
                nextDP.add(j)
                nextDP.add(j + nums[i])
                if target in nextDP:
                    return True
            dp = nextDP

        return True if target in dp else False


        