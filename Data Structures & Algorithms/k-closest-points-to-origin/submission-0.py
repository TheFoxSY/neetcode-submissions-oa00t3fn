import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = []
        res = []
        for i, point in enumerate(points):
            distance = math.sqrt((point[0] - 0) ** 2 + (point[1] - 0) ** 2)
            distances.append([distance, i])
        heapq.heapify(distances)

        for _ in range(k):
            index = heapq.heappop(distances)[1]
            res.append(points[index])
        
        return res
        
        