class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        def backtrack(path, nums , i):
            if i == len(nums):
                res.append(path[:])
                return
            
            path.append(nums[i])
            backtrack(path, nums, i + 1)
            path.pop()

            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            backtrack(path, nums, i + 1)



        backtrack([], nums, 0)
        return res
        