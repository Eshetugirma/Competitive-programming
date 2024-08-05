# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        arr = []
        count = 0
        while curr:
            if curr.val:
                count += curr.val
            else:
                if count:
                    arr.append(count)
                    count = 0
            curr = curr.next
        # print(arr)
        head = ListNode(0)
        
        dummy = head
        node = dummy

        for num in arr:
            
            curr = ListNode(num)
            node.next = curr
            curr.next = None
            node = node.next
            

        return head.next
        
                