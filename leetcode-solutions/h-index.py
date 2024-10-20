class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        n = len(citations)
        h_index = 0
        for i in range(n):
            if citations[n-i-1] > i:
                h_index += 1
        return h_index