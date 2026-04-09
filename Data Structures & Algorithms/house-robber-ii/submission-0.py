class Solution:
    def rob(self, nums: List[int]) -> int:
        return max(nums[0], self.hrob1(nums[1:]), self.hrob1(nums[:-1]))
    

    def hrob1(self, nums):
        rob1 ,rob2 = 0 , 0  #[rob1, rob2, n]
        for i in nums:
            temp = max(i + rob1, rob2)
            rob1 = rob2
            rob2 = temp
        return rob2
            
        