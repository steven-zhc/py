# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from data import ListNode
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        
        prev = ListNode(-101)
        prev.next = head

        root = prev
        curr = head
        
        while curr:
            if prev.val == curr.val:
                prev.next = curr.next
            else:
                prev = prev.next
            curr = curr.next
        
        return root.next
