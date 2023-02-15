# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        new = ListNode()
        head = new
        head1 = list1
        head2 = list2
        #==>>>> add every less Node in both list iteratevly
        while head1 and head2:
            if head1.val <= head2.val:
                head.next = head1
                head1 = head1.next
                head = head.next
            else:
                head.next = head2
                head2 = head2.next
                head = head.next
        if head1:
            head.next = head1
        else:
            head.next = head2
        return new.next