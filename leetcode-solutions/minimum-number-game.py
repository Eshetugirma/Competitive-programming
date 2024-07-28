class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        heap = nums
        arr = []
        heapify(heap)
        while heap:
            a,b = heappop(heap),heappop(heap)
            arr.append(b)
            arr.append(a)
        return arr
