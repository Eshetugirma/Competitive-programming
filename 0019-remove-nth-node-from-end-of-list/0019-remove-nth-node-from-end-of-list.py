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
        lenght = 1
        while new.next:
            lenght +=1
            new = new.next
        while count < n:
            curr = curr.next
            count+=1
        current = head
        while curr.next and curr.next.next:
            curr = curr.next
            current = current.next
        if lenght==n:
            return head.next
        current.next = current.next.next
        return head
            
        