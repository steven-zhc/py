class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        if not root:
            return None
        if root.val <= p.val:
            return self.inorderSuccessor(root.right, p)
        left = self.inorderSuccessor(root.left, p)
        if left:
            return left
        else:
            return root