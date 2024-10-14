class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        heap = []
        for num in nums:
            heappush(heap,-num)
        total = 0
        while k:
            curr = -(heappop(heap))
            total += curr
            heappush(heap,-(ceil(curr/3)))
            k -= 1
        return total

