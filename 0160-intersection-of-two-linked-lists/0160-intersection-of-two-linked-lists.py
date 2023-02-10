# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        curr1 = headA
        curr2 = headB
        length1 = 0
        diff1 = 0
        diff2 = 0
        #===>>>> iterate list to get length of headA
        while curr1:
            curr1 = curr1.next
            length1 += 1
        length2 = 0
        #===>>>> iterate list to get length of headB
        while curr2:
            curr2 = curr2.next
            length2 += 1
        #==>>> check the greater length and take difference of lengths
        if length1 > length2:
            diff1 = length1 - length2
        else:
            diff2 = length2 - length1
        curr1 = headA
        #===>>> go a head up to the difference between lengths
        while diff1:
            curr1 = curr1.next
            diff1 -= 1
        curr2 = headB
        while diff2:
            curr2 = curr2.next
            diff2 -= 1
        #===>>>> check the intersection node for lists
        while curr1 and curr2:
            if curr1 == curr2:
                return curr2
            curr1 = curr1.next
            curr2 = curr2.next

        