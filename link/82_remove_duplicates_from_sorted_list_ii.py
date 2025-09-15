# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        root = ListNode(-101, head)
        prev, curr = root, head

        while curr:
            if curr.next and curr.val == curr.next.val:
                v = curr.val
                while curr and curr.val == v:
                    curr = curr.next
                prev.next = curr
            else:
                prev = prev.next
                curr = curr.next

        return root.next


        