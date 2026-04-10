class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col = set()
        negDia = set()
        posDia = set()
        board = [["."] * n for _ in range(n)]
        res = []

        def backtrack(row):
            if row == n:
                copy = ["".join(rows) for rows in board]
                res.append(copy)
                return
            
            for c in range(n):
                if c in col or row + c in posDia or row - c in negDia:
                    continue
                
                board[row][c] = "Q"
                col.add(c)
                posDia.add(row + c)
                negDia.add(row - c)

                backtrack(row + 1)

                board[row][c] = "."
                col.remove(c)
                posDia.remove(row + c)
                negDia.remove(row - c) 
        
        backtrack(0)
        return res
        
        