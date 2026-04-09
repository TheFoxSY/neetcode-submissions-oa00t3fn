class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top, bottom = 0, len(matrix) - 1
        l, r = 0, len(matrix[0]) - 1

        while top <= bottom:
            mid = top + ((bottom - top) // 2)
            if matrix[mid][-1] < target :
                top = mid + 1
            elif matrix[mid][0] > target:
                bottom = mid - 1
            else:
                break
        
        if not (top <= bottom):
            return False
        
        currentRow = top + ((bottom - top) // 2)

        while l <= r:
            mid = l + ((r - l) // 2)
            if target < matrix[currentRow][mid]:
                r = mid - 1
            elif target > matrix[currentRow][mid]:
                l = mid + 1
            else:
                return True
        return False
