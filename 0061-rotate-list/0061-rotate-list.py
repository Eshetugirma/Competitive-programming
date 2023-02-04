# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        current = head 
        length = 1
        if not head or not head.next :
            return head
        while current.next:
            current=current.next
            length += 1
        current.next = head
        circular = head
        n = k%length
        while length - n-1:
            circular = circular.next
            
            n+=1
        ans = circular.next
        circular.next = None
        return ans
            
        
