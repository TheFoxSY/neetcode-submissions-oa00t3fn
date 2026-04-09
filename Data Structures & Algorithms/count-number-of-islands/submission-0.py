class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        res = 0

        def dfs(row, col):
            if (row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]) or grid[row][col] == "0"):
                return 
            
            grid[row][col] = "0"
            
            for dr, dc in directions:
                dfs(row + dr, col + dc)

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1":
                    dfs(r,c)
                    res += 1
        
        return res
        