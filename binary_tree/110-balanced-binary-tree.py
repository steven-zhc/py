class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        if abs(self.maxHeight(root.left) - self.maxHeight(root.right)) > 1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)

    def maxHeight(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        return max(self.maxHeight(root.left), self.maxHeight(root.right)) + 1