# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode],head=None,dummy=None) -> Optional[ListNode]:
        #==>> create head node and hold in dummy 
        if not head:
            head = ListNode()
            dummy = head
        #==>> if both list hold element then add the minimum to head 
        if list1 and list2:
            if list1.val <= list2.val:
                head.next = ListNode(list1.val)
                return self.mergeTwoLists(list1.next,list2,head.next,dummy)
            else:
                head.next = ListNode(list2.val)
                return self.mergeTwoLists(list1,list2.next,head.next,dummy)
        #==>>> when one of list element is empty then add non empity list to head 
        if list1:
            head.next = list1
        else:
            head.next = list2
        #==>> now return next of your dummy which is the sorted one 
        return dummy.next