class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        min_collector = [float('inf')]*n
        min_collector[k-1] = 0
        for _ in range(n-1):
            for current in times:
                min_collector[current[1]-1] = min(min_collector[current[0]-1]+current[2],min_collector[current[1]-1])
        ans = max(min_collector)
        return ans if ans != float('inf') else -1