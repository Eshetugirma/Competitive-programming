class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        ans = []
        for i in range(len(piles)//3):
            piles.pop()
            piles.remove(piles[0])
            ans.append(piles.pop())
        return sum(ans)
        