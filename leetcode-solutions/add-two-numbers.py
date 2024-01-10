# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr = l1
        temp1 = ""
        temp2 = ""
        #==>>> hold as string elements in l1
        while curr:
            temp1 += str(curr.val)
            curr = curr.next
        curr = l2
        #===>>> hold as string elements in l2
        while curr:
            temp2 += str(curr.val)
            curr = curr.next
        temp1 = temp1[::-1]
        temp2 = temp2[::-1]
        #==>>> integer sum of two string
        sums = str(int(temp1)+int(temp2))[::-1]
        ans = ListNode()
        curr = ans
        #==>>> constract linked list from sum of both list
        for i in sums:
            curr.next = ListNode(i)
            curr = curr.next
        return ans.next