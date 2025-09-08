# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, root: Optional[TreeNode]) -> list[list[int]]:
        if not root:
            return []
        # If it's a leaf node, return just the value
        if not root.left and not root.right:
            return [[root.val]]
        
        left, right = self.helper(root.left), self.helper(root.right)
        ext = lambda xs: [root.val] + xs
        return [*map(ext, left + right)]

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        result = self.helper(root)
        if not result:
            return []
        
        return [xs for xs in result if sum(xs) == targetSum]