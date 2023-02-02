# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        curr = head
        prev = ListNode(0)
        new_prev = ListNode(0)
        new_prev_head = new_prev
        prev_head = prev     
        while curr:
            if curr.val < x:
                # ===>>> add the smaller 
                prev_head.next = curr
                curr = curr.next
                prev_head = prev_head.next
                prev_head.next = None
            else:
                # ==>>> add the greater 
                new_prev_head.next = curr
                curr = curr.next
                new_prev_head = new_prev_head.next
                new_prev_head.next = None  
            prev_head.next = new_prev.next
        return prev.next