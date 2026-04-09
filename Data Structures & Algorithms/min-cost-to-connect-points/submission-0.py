class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)
        adj = {i : [] for i in range(N)}

        for i in range(N):
            x1, y1 = points[i]
            for j in range(i + 1, N):
                x2, y2 = points[j]
                distance = abs(x1 - x2) + abs(y1 - y2)
                adj[i].append([distance, j])
                adj[j].append([distance, i])
        
        res = 0
        visited = set()
        minHeap = [[0, 0]]
        while len(visited) < N:
            dist, point = heapq.heappop(minHeap)
            if point in visited:
                continue
            visited.add(point)
            res += dist
            for neiDist, nei in adj[point]:
                if nei not in visited:
                    heapq.heappush(minHeap, [neiDist, nei])
        return res
            
