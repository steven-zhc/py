# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        prev, curr = None, root
        stack, result = [], []

        while stack or curr:
            if curr:
                stack.append(curr)
                curr = curr.left
            else:
                curr = stack[-1]
                if curr.right is None or prev == curr.right:
                    result.append(curr.val)
                    stack.pop()
                    prev = curr
                    curr = None
                else:
                    curr = curr.right
        
        return result
                    
v