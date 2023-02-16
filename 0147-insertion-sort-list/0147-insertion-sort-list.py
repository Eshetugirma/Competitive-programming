# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = ListNode(-111111111111)
        prev.next = head
        curr = prev.next
        #==>>> move every element and find unsorted node
        while curr and curr.next:
            if curr.val > curr.next.val:
                temp = curr.next
                curr.next = curr.next.next
                new = prev
                #===>>> hold unsorted node and put it in respective place
                while new :
                    if new.next.val > temp.val:
                        temp.next = new.next
                        new.next = temp
                        break
                    new = new.next
            #==>>> for element those sorted then move the pointer
            else:
                curr = curr.next
        return prev.next
                    
                        
                        
        