# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        curr = node
        #===>>>copy the value of given linkedlist one step back starting from given node 
        while curr.next and curr.next.next:
            curr.val = curr.next.val
            curr = curr.next
        curr.val = curr.next.val
        #====>>>>>then delete the last node
        curr.next = None
                
        