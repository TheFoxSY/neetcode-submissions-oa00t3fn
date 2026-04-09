class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def dfs(total, target, path, index):
            if total == target:
                res.append(path[:])
                return
            if total > target or index == len(candidates):
                return
            
            path.append(candidates[index])
            dfs(total + candidates[index], target, path, index + 1)
            path.pop()

            while index + 1 < len(candidates) and candidates[index] == candidates[index + 1]:
                index += 1
            dfs(total, target, path, index + 1)

            
        dfs(0, target, [], 0)
        return res
        