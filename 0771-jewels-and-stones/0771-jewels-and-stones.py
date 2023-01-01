class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        my_dict = {}
        count = 0
        for i,v in enumerate(jewels):
            my_dict[v] = i
        for stone in stones:
            if stone in my_dict:
                count += 1
                
        return count
        