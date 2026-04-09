class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        
        def dfs(total, target, path, i):
            if total == target:
                res.append(path[:])
                return
            if i >= len(nums) or total > target:
                return

            path.append(nums[i])

            dfs(total + nums[i], target, path, i)
            path.pop()
            dfs(total, target, path, i + 1)

        dfs(0, target, [], 0)
        return res

        
        


            
        