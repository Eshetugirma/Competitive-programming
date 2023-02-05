# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head 
        new = ListNode(0.1)
        temp = []
        count = 1
        if not head:
            return head
        new.next = head
        current = new
        #===>>>>> find the single number that never repeated in the sorted list then add to temp 
        while current.next and current.next.next:
            if current.val != current.next.val and current.next.val != current.next.next.val:
                temp.append(current.next.val)
            current = current.next
            count +=1
        if current.val != current.next.val:
            temp.append(current.next.val)
        #==>>>> this is to form new linked list that hold my answer using element in temp
        if not head.next:
            return head
        ans = head
        for i in temp:
            ans.val = i
            ans = ans.next
        #===>>>>> if there is no element in temp then return 
        if len(temp)==0:
            return
        # ====>>>> if there is duplicate element then cut others from new list 
        if count != len(temp):
            ans = head
            for i in temp:
                ans.val = i
                ans = ans.next
            ans.next = None
            ans = head
            while ans.next and ans.next.next:
                ans = ans.next
            ans.next = None                 
        return head