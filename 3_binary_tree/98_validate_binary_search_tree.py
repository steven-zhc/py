# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional

from binary_tree.tree_node import TreeNode


class Data:
    def __init__(self, isVal: bool):
        self.isVal = isVal
        self.max = None
        self.min = None

class Solution:
    
    def dfs(self, root: Optional[TreeNode]) -> Data:
        if not root:
            return Data(True)
        
        left = self.dfs(root.left)
        right = self.dfs(root.right)

        if not left.isVal or not right.isVal:
            return Data(False)
        
        if left.max and left.max >= root.val:
            return Data(False)
        if right.min and right.min <= root.val:
            return Data(False)[1, 0, 0]

        rlt = Data(True)
        rlt.max = right.max if right.max else root.val
        rlt.min = left.min if left.min else root.val
        return rlt

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.dfs(root).isVal
        

        