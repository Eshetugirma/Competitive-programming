class Solution:
    def maximumScore(self, a: int, b: int, c: int) -> int:
        heap = [-a,-b,-c]
        heapify(heap)
        count = 0
        stone = 3
        while stone > 1:
            a1,b1 = -heappop(heap)-1,-heappop(heap)-1
            if a1 > 0:
                heappush(heap,-a1)
            else:
                stone -= 1
            if b1 > 0:
                heappush(heap,-b1)
            else:
                stone -= 1

            count += 1
        return count
