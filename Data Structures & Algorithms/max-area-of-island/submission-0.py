class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [[-1,0], [0,-1], [1,0], [0,1]]
        res = 0

        def dfs(rows, cols):
            if (rows < 0 or rows >= len(grid) or cols < 0 or cols >= len(grid[0]) or grid[rows][cols] == 0):
                return 0
            
            area = 1
            grid[rows][cols] = 0

            for r_dir, c_dir in directions:
                area += dfs(rows + r_dir, cols + c_dir)
            return area
        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    res = max(res, dfs(r,c))
        return res
        