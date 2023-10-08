# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        root = head
        arr = []
        seen = set()
        while root:
            arr.append(root.val)
            root = root.next
        for i in range(len(arr)):
            temp = set()
            running_sum = 0
            for j in range(i,len(arr)):
                temp.add(j)

                if j not in seen:
                    running_sum += arr[j]
                if not running_sum:
                    seen = seen.union(temp)
                    break
        ans = []
        for i in range(len(arr)):
            if i not in seen:
                ans.append(arr[i])
        a = root
        root = ListNode()
        temp = root
        temp.next = None
        curr = root

        for num in ans:
            curr.next = ListNode(num)
            curr = curr.next
        return root.next