# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False
        
        
        if root.val == subRoot.val:
            if self.isSameTree(root, subRoot):
                return True

        return (self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot))


    def isSameTree(self, original, sub):
        if not original and not sub:
            return True
        if original and sub and original.val == sub.val:
            return (self.isSameTree(original.left , sub.left) and self.isSameTree(original.right, sub.right))
        return False 
