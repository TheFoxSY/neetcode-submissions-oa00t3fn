class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        res = 0
        leftMax = height[0]
        rightMax = height[len(height) - 1]
        
        if not height:
            return 0

        while left < right:

            if leftMax < rightMax:
                left += 1
                leftMax = max(leftMax, height[left])
                res += leftMax - height[left]
            else:
                right -= 1
                rightMax = max(rightMax, height[right])
                res += rightMax - height[right]
        
        return res


        
        