from sortedcontainers import SortedList
class StockPrice:

    def __init__(self):
        self.sorted_list = SortedList()
        self.dict = defaultdict(int)
        self.curr = SortedList()

        

    def update(self, timestamp: int, price: int) -> None:
        self.curr.add(timestamp)
        if timestamp in self.dict:
            self.sorted_list.remove(self.dict[timestamp])
            self.sorted_list.add(price)
            self.dict[timestamp] = price
        else:
            self.sorted_list.add(price)
            self.dict[timestamp] = price
        
            
    def current(self) -> int:
        # print(self.sorted_list)
        return self.dict[self.curr[-1]]

    def maximum(self) -> int:
        # print(self.sorted_list)
        return self.sorted_list[-1]
        

    def minimum(self) -> int:
        # print(self.sorted_list)
        return self.sorted_list[0]
        


# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()