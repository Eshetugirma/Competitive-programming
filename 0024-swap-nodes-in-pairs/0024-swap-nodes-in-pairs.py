# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        prev = None
        ans = ListNode()
        move = ans
        #==>>> if empty or single node return itself
        if not curr or not curr.next:
            return head
        #===>>> swap every adjecent node and story it to ans
        while curr and curr.next:
            prev = curr.next
            curr.next = curr.next.next
            prev.next = curr
            curr = curr.next
            move.next = prev
            move = move.next.next
        return ans.next