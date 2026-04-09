class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        if not heights:
            return 0
        
        res = 0

        for i in range(len(heights)):
            l , r = i - 1, i + 1
            width = 1
            curHeight = heights[i]
            while l >= 0:
                if heights[l] >= heights[i]:
                    width += 1
                    l -= 1
                else: break
                
            
            while r < len(heights):
                if heights[r] >= heights[i]:
                    width += 1
                    r += 1
                else: break
            
            area = width * curHeight
            res = max(res, area)
        
        return res

        


                    
                    