class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l , r = 1, max(piles)
        res = r
        
        
        while l <= r:
            k = l + ((r - l) // 2)
            time = 0
            for num in piles:
                time += math.ceil(num / k)
            if time <= h:
                r = k - 1
                res = k
            else:
                l = k + 1
        return res

                
                

