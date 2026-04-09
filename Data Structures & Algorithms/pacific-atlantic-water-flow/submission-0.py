class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights) , len(heights[0])
        pac , alt = set(), set()
        res = []
        directions = [[1,0], [-1,0], [0,1], [0,-1]]

        def dfs(row, col, visited, prevHeight):
            if ((row,col) in visited or row < 0 or col < 0 
                or row == rows or col == cols or heights[row][col] < prevHeight):
                return
            visited.add((row,col))
            for dr, dc in directions:
                dfs(row + dr, col + dc, visited, heights[row][col])

        for r in range(rows):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, cols - 1, alt, heights[r][cols - 1])
        
        for c in range(cols):
            dfs(0, c, pac, heights[0][c])
            dfs(rows - 1, c, alt, heights[rows - 1][c])
        
        for r in range(rows):
            for c in range(cols):
                if (r,c) in pac and (r,c) in alt:
                    res.append([r,c])
        return res
            

        