class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        newNums = [-num for num in nums]
        heapq.heapify(newNums)
        for i in range(k):
            cur = heapq.heappop(newNums)
            if i == k - 1:
                if cur > 0:
                    return 0 - cur
                return abs(cur)
        