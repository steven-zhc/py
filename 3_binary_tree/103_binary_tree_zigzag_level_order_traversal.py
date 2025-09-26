# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        result = []
        flag = True

        from collections import deque
        q = deque([root])
        while q:
            level = deque()
            for _ in range(len(q)):
                n = q.popleft()
                if flag:
                    level.append(n.val)
                else:
                    level.appendleft(n.val)
                if n.left:
                    q.append(n.left)
                if n.right:
                    q.append(n.right)
            result.append(list(level))
            flag = not flag
        
        return result
        