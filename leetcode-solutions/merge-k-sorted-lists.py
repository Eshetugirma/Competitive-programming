# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        dummy = ans = ListNode(0)

        for i in range(len(lists)):
            curr = lists[i]
            if curr:
                heappush(heap,(curr.val,i,curr))
        while heap:
            val,index,node = heappop(heap)
            dummy.next = ListNode(val)
            dummy = dummy.next
            if node.next:
                heappush(heap,(node.next.val,index,node.next))
        return ans.next
        