class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stone = [-s for s in stones]
        heapq.heapify(stone)
        while len(stone) > 1:
            x , y = heapq.heappop(stone) , heapq.heappop(stone)
            if x - y != 0:
                heapq.heappush(stone, x - y)
    
        return abs(stone[0]) if stone else 0    
            

        