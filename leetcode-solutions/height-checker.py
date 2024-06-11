class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected = sorted(heights)
        unOrdered = 0
        for i in range(len(heights)):
            if expected[i] != heights[i]:
                unOrdered += 1
        return unOrdered
        