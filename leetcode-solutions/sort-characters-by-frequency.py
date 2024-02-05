class Solution:
    def frequencySort(self, s: str) -> str:
        counts = Counter(s)
        heap = []
        for k,v in counts.items():
            heappush(heap,(v,k))
        sorted_s = []
        while heap:
            pair = heappop(heap)
            sorted_s.append(pair[0]*pair[1])
        sorted_s.reverse()
        return ''.join(sorted_s)
        