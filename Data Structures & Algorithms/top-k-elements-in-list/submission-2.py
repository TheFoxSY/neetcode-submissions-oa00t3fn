import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for n in nums:
            count[n]=1+count.get(n, 0)
        
        heap=[]
        
        for number,freq in count.items():
            if len(heap)<k:
                heapq.heappush(heap, (freq, number))
            else:
                heapq.heappushpop(heap, (freq, number))
        
        result=[]
        for i in range(k):
            result.append(heapq.heappop(heap)[1])

        return result

        

        