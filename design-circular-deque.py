class Node:
    def __init__(self, val, p=None, n=None):
        self.val = val
        self.prev = p
        self.next = n
class MyCircularDeque:
    def __init__(self, k: int):
        self.k = k
        self.l = 0
        self.head = self.tail = None

    def insertFront(self, value: int) -> bool:
        if(self.l == self.k):
            return 0
        if(self.l == 0):
            self.head = self.tail = Node(value)
        else:
            curr = Node(value)
            self.head.prev, curr.next = curr, self.head
            self.head = curr
        self.l += 1
        return 1
        

    def insertLast(self, value: int) -> bool:
        if(self.l == self.k):
            return 0
        if(self.l == 0):
            self.head = self.tail = Node(value)
        else:
            curr = Node(value)
            self.tail.next, curr.prev = curr, self.tail
            self.tail = curr
        self.l += 1
        return 1

    def deleteFront(self) -> bool:
        if(self.l == 0):
            return 0
        self.head = self.head.next
        self.l -= 1
        return 1

    def deleteLast(self) -> bool:
        if(self.l == 0):
            return 0
        self.tail = self.tail.prev
        self.l -= 1
        return 1

    def getFront(self) -> int:
        if(self.l == 0):
            return -1
        return self.head.val

    def getRear(self) -> int:
        if(self.l == 0):
            return -1
        return self.tail.val

    def isEmpty(self) -> bool:
        return self.l == 0

    def isFull(self) -> bool:
        return self.l == self.k