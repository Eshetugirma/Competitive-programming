class Solution:
    def hIndex(self, citations: List[int]) -> int:
        left = 0
        right = len(citations)
        while right > left:
            mid = (left + right)//2
            if len(citations) - mid == citations[mid]:
                return len(citations)-mid
            if len(citations) - mid < citations[mid]:
                right = mid
            else:
                left = mid+1
        return len(citations)-left