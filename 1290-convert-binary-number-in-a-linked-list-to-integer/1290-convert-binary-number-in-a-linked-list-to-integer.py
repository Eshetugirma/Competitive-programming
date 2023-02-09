# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        current_head = head
        prev = None
        #===>>>> first reverse list to get least significant bit at head
        while current_head:
            temp = current_head.next
            current_head.next = prev
            prev = current_head
            current_head = temp
        current_head = prev
        ans = 0
        exp = 0
        #===>>> convert binary to decimal directly 
        while current_head:
            ans += pow(2,exp)*current_head.val
            current_head = current_head.next
            exp += 1
        return ans
            
             
            
        