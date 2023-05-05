class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        heap = []
        for row in matrix:
            row.reverse()
            heappush(heap,(row.pop(),0,row))
        for i in range(k):
            curr = heappop(heap)
            if curr[2]:
                heappush(heap,(curr[2].pop(),0,curr[2]))
        return curr[0]