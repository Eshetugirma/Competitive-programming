class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        # if numBottles == numExchange: return numBottles + 1
        # elif numBottles < numExchange: return numBottles
        return numBottles + (numBottles-1)//(numExchange-1)