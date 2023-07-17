# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        stack1 = []
        stack2 = []
        head = l1
        while head:
            stack1.append(str(head.val))
            head = head.next 

        head = l2
        while head:
            stack2.append(str(head.val))
            head = head.next
        temp = int("".join(stack1)) + int("".join(stack2))
        temp = list(str(temp))
        head = ans = ListNode(0)
        for i in temp:
            head.next = ListNode(int(i))
            head = head.next
        return ans.next