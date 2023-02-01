# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        prev = None
        #===>>> to find the middle point of linked list which (slow) is middle point
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        #==>>> reverse list after middle point
        while slow:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp  
        right, left = prev,head
        #==>>> check if palindrome
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        return True
    