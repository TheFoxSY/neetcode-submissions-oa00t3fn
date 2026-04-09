class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left , right = 0 , len(nums) - 1
        mid = left + ((right- left) // 2)

        while left <= right:
            if nums[mid] > target:
                right = mid - 1
                mid = left + ((right- left) // 2)
            elif nums[mid] < target:
                left = mid + 1 
                mid = left + ((right- left) // 2)
            else:
                return mid
        
        return -1
            
        