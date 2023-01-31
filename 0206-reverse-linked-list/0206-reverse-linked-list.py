# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
'''
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head :
            return None
        new_head = head
        if head.next:
            #===>>>> done recursivly by spliting to small piece
            new_head = self.reverseList(head.next)
            head.next.next = head
        head.next = None
        return new_head
        '''
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current_head = head
        prev_head = None
        while current_head:
            #==>> iterative mothed updating current head to next and converting head to tail
            temp = current_head.next
            current_head.next = prev_head
            prev_head = current_head
            current_head = temp
        return prev_head
            
        