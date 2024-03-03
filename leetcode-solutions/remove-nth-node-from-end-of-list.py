# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        curr = head 
        count = 1
        new = head
        length = 1
        while new.next:
            length +=1
            new = new.next
        length -= n
        if not length: return head.next
        while length > 1:
            curr = curr.next
            
            length -=1
        if curr.next:
            curr.next = curr.next.next
        else:
            return None

        return head 

  