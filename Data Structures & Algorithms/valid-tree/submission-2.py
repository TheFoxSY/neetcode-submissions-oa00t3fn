class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) > (n - 1):
            return False

        adj = {i : [] for i in range(n)}

        visited = set()
        for edge1, edge2 in edges:
            adj[edge1].append(edge2)
            adj[edge2].append(edge1)
        
        def dfs(node,prevNode):
            if node in visited:
                return False

            visited.add(node)
            for nei in adj[node]:
                if nei == prevNode:
                    continue
                if not dfs(nei,node):
                    return False  
            return True
                
        return dfs(0,-1) and len(visited) == n
        