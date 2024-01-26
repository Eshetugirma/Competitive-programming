class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        count = 0
        while target > 1 and maxDoubles :
            count = count + target%2 + 1
            maxDoubles -= 1 
            target //= 2
        return count + target - 1

        