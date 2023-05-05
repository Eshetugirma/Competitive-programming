class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        heap = []
        for num in piles:
            heappush(heap,-num)
        for i in range(k):
            pop = heappop(heap)
            heappush(heap,pop//2)
        return -sum(heap)