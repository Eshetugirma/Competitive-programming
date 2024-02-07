class Solution:
    def maxSpending(self, values: List[List[int]]) -> int:
        heap = []
        for i in range(len(values)):
            for j in range(len(values[0])):
                heappush(heap,values[i][j])
        cur_day, ans = 1,0
        while heap:
            ans += cur_day*heappop(heap)
            cur_day += 1
        return ans