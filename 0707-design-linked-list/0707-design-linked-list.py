class Node:
    def __init__(self,val):
        self.val = val
        self.next = None
class MyLinkedList:

    def __init__(self):
        self.head = None
        self.size = 0
        
    def get(self, index: int) -> int:
        if not self.head:
            return -1
        current_node = self.head
        current_index = 0
        while current_index < index :
            if not current_node.next:
                return -1
            current_node = current_node.next
            current_index +=1
        return current_node.val
    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)
    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size, val)
    def addAtIndex(self, index: int, val: int) -> None:
        
        if index > self.size:
            return
        current = self.head
        new_node = ListNode(val)

        if index <= 0:
            new_node.next = current
            self.head = new_node
        else:
            for _ in range(index - 1):
                current = current.next
            new_node.next = current.next
            current.next = new_node
        self.size += 1
    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
        current = self.head
        if index == 0:
            self.head = self.head.next
        else:
            for _ in range(0, index - 1):
                current = current.next
            current.next = current.next.next
        self.size -= 1
# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
