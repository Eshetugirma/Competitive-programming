class StockSpanner:

    def __init__(self):
        #===>>> define stack to hold element monotonic decreasing 
        self.stack = []
        
    def next(self, price: int) -> int:
        freq = 1
        #===>>>>> count on freq how many of price we see those less or equal to current price
        while self.stack and self.stack[-1][0] <= price:
            freq += self.stack[-1][1]
            self.stack.pop()
        self.stack.append([price,freq])
        return freq

        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)