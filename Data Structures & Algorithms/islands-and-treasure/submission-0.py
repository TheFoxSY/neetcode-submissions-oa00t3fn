class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        row, col = len(grid), len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        INF = 2147483647

        def bfs(rows, cols):
            q = collections.deque([(r,c)])
            visited = [[False] * col for _ in range(row)]
            visited[r][c] = True
            steps = 0
            while q:
                for _ in range(len(q)):
                    Row , Col = q.popleft()
                    if grid[Row][Col] == 0:
                        return steps
                    for dr , dc in directions:
                        nr , nc = Row + dr, Col + dc
                        if (0 <= nr < row and 0 <= nc < col and
                            not visited[nr][nc] and grid[nr][nc] != -1):
                            visited[nr][nc] = True
                            q.append((nr, nc))
                steps += 1
            return INF

        for r in range(row):
            for c in range(col):
                if grid[r][c] == INF:
                    grid[r][c] = bfs(r,c)

        