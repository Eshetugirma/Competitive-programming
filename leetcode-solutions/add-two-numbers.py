# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        carry = 0
        sum_list = ListNode(0)
        t = sum_list
        head = t
        while l1 and l2:
            curr = l1.val + l2.val + carry
            if curr > 9:
                carry = 1
                curr %= 10
            else:
                carry = 0
            sum_list.next = ListNode(curr)
            sum_list =sum_list.next
            l1 = l1.next
            l2 = l2.next


        while l1:
            curr = l1.val + carry
            if curr > 9:
                carry = 1
                curr %= 10
            else:
                carry = 0
            sum_list.next = ListNode(curr)
            sum_list =sum_list.next
            l1 = l1.next


        while l2:
            curr = l2.val + carry
            if curr > 9:
                carry = 1
                curr %= 10
            else:
                carry = 0
            sum_list.next = ListNode(curr)
            sum_list =sum_list.next
            l2 = l2.next


        if carry:
            sum_list.next = ListNode(1)

        return head.next
            