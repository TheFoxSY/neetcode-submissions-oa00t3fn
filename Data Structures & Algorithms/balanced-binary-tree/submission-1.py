# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(root):
            if not root:
                return [True, 0]
            
            leftDepth = dfs(root.left)
            rightDepth = dfs(root.right)

            balanced = (leftDepth[0] and rightDepth[0] and 
            abs(leftDepth[1] - rightDepth[1]) <= 1)
            
            return [balanced, 1 + max(leftDepth[1], rightDepth[1])]
        return dfs(root)[0] 
        