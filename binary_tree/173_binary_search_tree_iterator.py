# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.data = self.dfs(root)
        self.curr = -1
        

    def next(self) -> int:
        self.curr += 1
        return self.data[self.curr].val
        

    def hasNext(self) -> bool:
        n = self.curr + 1
        return True if 0 <= n < len(self.data) else False

    def dfs(self, root: Optional[TreeNode]) -> list[TreeNode]:
        if not root:
            return []
        
        return self.dfs(root.left) + [root] + self.dfs(root.right)
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()