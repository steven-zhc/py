# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        result = []
        stack = [root]
        while stack:
            n = stack.pop()
            result.append(n.val)

            if n.right:
                stack.append(n.right)
            if n.left:
                stack.append(n.left)
            
        return result