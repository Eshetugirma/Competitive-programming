# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = node = head 
        while curr.next:
            temp = curr.next
            curr.next = ListNode(gcd(curr.val,temp.val))
            curr.next.next = temp
            curr = curr.next.next
        return node
    
        