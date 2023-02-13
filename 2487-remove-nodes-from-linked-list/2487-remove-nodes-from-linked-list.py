# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        prev = None
        #==>>> this is to reverse the given list
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        curr = prev
        #===>>> delate if the next node is less than this node else move forward
        while curr and curr.next:
            if curr.val > curr.next.val:
                curr.next = curr.next.next
            else:
                curr = curr.next
        curr = prev
        prev = None
        #==>>>> reverse the list to get their original position
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp 
        return prev