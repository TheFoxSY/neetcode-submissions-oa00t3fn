# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        queue = collections.deque([(root, root.val)])
        res = 0

        while queue:
            cur , maxval = queue.popleft()
            if cur.val >= maxval:
                res += 1
            maxval = max(cur.val, maxval)

            if cur.left:
                queue.append([cur.left, maxval])
            if cur.right:
                queue.append([cur.right, maxval])
        
        return res

        
        
        