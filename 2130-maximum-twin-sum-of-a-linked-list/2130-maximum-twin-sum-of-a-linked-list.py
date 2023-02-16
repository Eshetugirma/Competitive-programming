# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        curr = head
        res = []
        #===>>> append all linked list elements in res
        while curr:
            res.append(curr.val)
            curr = curr.next
        n = len(res)
        maximum = 0
        #==>>> find the greater twin in res
        for i in range(len(res)//2):
            twin = res[n-i-1] + res[i]
            if twin > maximum:
                maximum = twin
        return maximum