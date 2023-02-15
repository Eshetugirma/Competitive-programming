# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head
        if not head.next:
            return head.next
        # ==>>> using fast and slow pointer to see the medium pointer
        while fast and fast.next:
            fast = fast.next.next
            if fast and fast.next:
                slow = slow.next
        #===>>> delete the middle node of the list 
        slow.next = slow.next.next
        return head