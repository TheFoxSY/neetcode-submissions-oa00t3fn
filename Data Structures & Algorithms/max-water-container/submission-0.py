class Solution:
    def maxArea(self, heights: List[int]) -> int:
        totalRain = 0
        l, r = 0, len(heights) - 1

        while l < r:
            if heights[l] < heights[r]:
                height = heights[l]
                width = r - l
                totalRain = max(totalRain, height * width)
                l += 1
            else:
                height = heights[r]
                width = r - l
                totalRain = max(totalRain, height * width)
                r -= 1
        
        return totalRain


        