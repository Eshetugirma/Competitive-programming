# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        current_node = head
        prev = None
        current_index = 1
        # ===>>> my current node updated until i see the given left index
        if current_index == left:
            temp_prev = current_node
        while current_index < left:
            current_index +=1
            prev = current_node
            temp_prev = current_node
            current_node = current_node.next     
        temp_curr = current_node
        #====>>> now i reverse the node flow of connection until i get the given right index
        while current_index <=right:
            current_index +=1
            temp = current_node.next
            current_node.next = prev
            prev = current_node
            current_node = temp
        # ==>>> finally connect the neccessery node
        temp_prev.next = prev
        temp_curr.next = current_node
        #===>>>> if my head may changed this update head to new head that is equal to right position
        if left == 1:
            head = prev
        return head
