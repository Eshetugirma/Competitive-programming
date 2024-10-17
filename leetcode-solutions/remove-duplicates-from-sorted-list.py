
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr1 = head
        while curr1 and curr1.next:
            if curr1.val == curr1.next.val:
                curr1.next = curr1.next.next
            else:
                curr1 = curr1.next
        return head