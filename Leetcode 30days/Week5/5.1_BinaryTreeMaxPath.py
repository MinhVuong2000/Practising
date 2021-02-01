# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def oneSum(self, node: TreeNode) -> int:
        if not node:
            return 0
        l = max(0,self.oneSum(node.left))
        r = max(0,self.oneSum(node.right))
        self.res = max(self.res,node.val + l + r)
        return node.val + max(r,l)
    
    def maxPathSum(self, root: TreeNode) -> int:
        if not root:
            return 0
        self.res = root.val
        self.oneSum(root)
        return self.res
        
