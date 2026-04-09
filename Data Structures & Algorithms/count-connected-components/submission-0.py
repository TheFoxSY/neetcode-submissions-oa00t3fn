class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = {i : [] for i in range(n)}
        res = 0

        visited = set()
        for edge1, edge2 in edges:
            adj[edge1].append(edge2)
            adj[edge2].append(edge1)
        
        def dfs(node):

            visited.add(node)
            for nei in adj[node]:
                if nei not in visited:
                    dfs(nei)
            return True
        

        for i in range(n):
            if i not in visited:
                dfs(i)
                res += 1
        
        return res
        