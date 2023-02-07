# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #====>>>> return it self for the boundary case 
        if not head or not head.next or not head.next.next:
            return head
        odd = head
        even_head = head.next
        even = even_head
        #====>>>> hold separately both even and odd lists 
        while even and even.next:
            odd.next = odd.next.next
            odd = odd.next
            even.next = even.next.next
            even = even.next
        #===>>>> now join both even and odd lists then return it
        odd.next = even_head
        return head
