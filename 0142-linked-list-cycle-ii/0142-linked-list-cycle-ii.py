# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head
        #==>>> check if there is a cycle in list by fast and slow pointers
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
            #==>>> if there is cycle use start from head and move until pointer point to the same node that start points                
                start = head
                pointer = slow
                while start:
                    if start == pointer:
                        return pointer
                    start = start.next
                    pointer = pointer.next
            