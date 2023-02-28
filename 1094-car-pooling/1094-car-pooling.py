class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        offset = [0]*1001
        #==>> by diclaring offset add passanger at start and remove of at end index
        for pas,start,end in trips:
            offset[start] += pas
            offset[end] -= pas
        prefix_sum = 0
        #==>> take running sum of offset and check if it is out of our capacity
        for i in offset:
            prefix_sum = prefix_sum+i
            if prefix_sum > capacity:
                return False
        return True