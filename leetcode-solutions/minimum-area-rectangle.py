class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        min_area = float('inf')
        seen = set()
        for x,y in points:
            for x0,y0 in seen:
                if (x,y0) in seen and (x0,y) in seen:
                    min_area = min(min_area,abs(x-x0)*abs(y-y0))
            seen.add((x,y))
        return min_area if min_area != float('inf') else 0
        