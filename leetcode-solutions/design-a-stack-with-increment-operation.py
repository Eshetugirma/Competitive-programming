class CustomStack:

    def __init__(self, maxSize: int):
        self.stack = []
        self.size = maxSize
        

    def push(self, x: int) -> None:
        if self.size > len(self.stack):
            self.stack.append(x)

    def pop(self) -> int:
        
        return -1 if not self.stack else self.stack.pop()

        

    def increment(self, k: int, val: int) -> None:
        for i in range(min(len(self.stack),k)):
            self.stack[i] += val
        


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)