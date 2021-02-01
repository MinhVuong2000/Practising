# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertTree(self, pTree: TreeNode,value: int) -> TreeNode:
        if not pTree:
            pTree = TreeNode(value)
        elif pTree.val<value:
            pTree.right = self.insertTree(pTree.right, value)
        else: pTree.left = self.insertTree(pTree.left,value)
        return pTree
    
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        if not preorder:
            return None
        pTree = None
        for i in preorder:
            pTree = self.insertTree(pTree,i)
        return pTree
