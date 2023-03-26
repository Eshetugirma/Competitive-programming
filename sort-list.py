# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #====>>>>> this is not the best solution becouse it use space O(N) 
        stack = []
        curr = head
        while curr:
            stack.append(curr.val)
            curr = curr.next
        stack.sort()
        ans = ListNode(0)
        pointer = ans
        for i in range(len(stack)):
            pointer.next = ListNode(stack[i])
            pointer = pointer.next
        return ans.next