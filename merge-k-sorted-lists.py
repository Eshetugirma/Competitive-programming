# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        stack = []
        for head in lists:
            while head:
                stack.append(head.val)
                head = head.next
            
        stack.sort()
        new_list = ListNode(None)
        new_holder = new_list
        for nums in stack:
            new_holder.next = ListNode(nums)
            new_holder = new_holder.next

        return new_list.next